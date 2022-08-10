println("Importing...")
using EpistemicNetworkAnalysis
using CSV
using DataFrames
using Plots
using Colors
using Statistics
using HypothesisTests
using JSON
using Dates

const MODEL_DIR = Dates.format(now(), "yyyymmddHHMMSS")
mkdir("models/$MODEL_DIR")

let # local scope

println("Loading Data...")
data = DataFrame(CSV.File("data/preprocessed.csv", missingstring="NULL"))

println("Preprocessing data...")
sessionMap = Dict(
    session => index
    for (index, session) in enumerate(sort(unique(data[!, :Session])))
)

data[!, :SessionNum] = getindex.(Ref(sessionMap), data[!, :Session])
data[!, :All] .= "All"
data[!, :ActivityType] .= "Divergent"
data[data[!, :Convergent] .== 1, :ActivityType] .= "Convergent"

println("Defining basic model...")
conversations = [:Session, :Activity, :Group]
units = [:Session, :Speaker]
codes = [
    :AI,
    :Compare,
    :Manipulate,
    :Teach,
    :Performance,
    :Sequence,
    :Thinking,
    :Trust
]

windowSize = 16

println("Defining model options...")
prePostMR = MeansRotation(:Session, "#01 / pre", "#11 / post")
activityTypeMR = MeansRotation(:ActivityType, "Divergent", "Convergent")
sessionMCR_1_2 = MulticlassRotation(:Session, 1, 2)
sessionMCR_3_4 = MulticlassRotation(:Session, 3, 4)
probeToolkitM2R = Means2Rotation(:Probe, 0, 1, :Toolkit, 0, 1)
toolkitPrototypeM2R = Means2Rotation(:Toolkit, 0, 1, :Prototype, 0, 1)
prototypeProbeM2R = Means2Rotation(:Prototype, 0, 1, :Probe, 0, 1)
everythingFilter(row) = true
fellowFilter(row) = (row[:Role] == "Fellow")
prePostFellowFilter(row) = (row[:Role] == "Fellow" && row[:Session] in ["#01 / pre", "#11 / post"])
defaultColors = EpistemicNetworkAnalysis.DEFAULT_EXTRA_COLORS
sessionColors = RGB.(range(HSL(colorant"red"),
                           stop=HSL(colorant"green"),
                           length=length(unique(data[!, :Session]))))

println("Defining gamut...")
function gamut(name, bugfix, rotation, myFilter, colors)
    println("\tfor $name...")
    filename = "models/$MODEL_DIR/$name"
    myENA = ENAModel(data, codes, conversations, units,
                     windowSize=windowSize,
                     rotateBy=rotation,
                     subsetFilter=myFilter)

    open("$filename.json", "w") do f
        write(f, json(EpistemicNetworkAnalysis.test(myENA)))
    end

    GR.setarrowsize(1/bugfix) # BUGFIX: divide the default arrow size by ceil(sqrt(number of plots in the multi plot)) = number of plots on the first row
    p = plot(myENA, extraColors=colors, showUnits=false)
    savefig(p, "$filename.png")
    p = plot(myENA, extraColors=colors, leg=nothing)
    savefig(p, "$(filename)_no_legend.png")
    p = plot(myENA, extraColors=colors, leg=nothing,  showCIs=false, showNetworkLines=false, showTrajectoryBy=:SessionNum, spectralColorBy=:SessionNum)
    savefig(p, "$(filename)_hairball.png")
end

println("Running gamuts...")
gamut("mr_pre_post", 2, prePostMR, prePostFellowFilter, defaultColors)
gamut("mr_divergent", 2, activityTypeMR, fellowFilter, defaultColors)
gamut("mcr_1_2", 9, sessionMCR_1_2, fellowFilter, sessionColors)
gamut("mcr_3_4", 9, sessionMCR_3_4, fellowFilter, sessionColors)
gamut("m2r_probe_toolkit", 2, probeToolkitM2R, fellowFilter, defaultColors)
gamut("m2r_toolkit_proto", 2, toolkitPrototypeM2R, fellowFilter, defaultColors)
gamut("m2r_proto_probe", 2, prototypeProbeM2R, fellowFilter, defaultColors)

println("Done!")

end # let