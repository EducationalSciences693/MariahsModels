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

# const MODEL_DIR = "test"
const MODEL_DIR = Dates.format(now(), "yyyymmddHHMMSS")
mkpath("models/$MODEL_DIR")

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
    :Alert,
    :AI,
    :Compare,
    :Construct,
    :Groups,
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
                           stop=HSL(colorant"blue"),
                           length=length(unique(data[!, :Session]))))

println("Defining gamut...")
function gamut(name, rotation, myFilter, colors, lims)
    println("\tfor $name...")
    filename = "models/$MODEL_DIR/$name"
    myENA = ENAModel(data, codes, conversations, units,
                     windowSize=windowSize,
                     rotateBy=rotation,
                     subsetFilter=myFilter)

    open("$filename.json", "w") do f
        write(f, json(EpistemicNetworkAnalysis.test(myENA)))
    end

    p = plot(myENA, lims=lims, extraColors=colors, showUnits=false)
    savefig(p, "$filename.png")
    p = plot(myENA, lims=lims, extraColors=colors, leg=nothing)
    savefig(p, "$(filename)_no_legend.png")

    GR.setarrowsize(1/9) # BUGFIX: divide the default arrow size by ceil(sqrt(number of plots in the multi plot)) = number of plots on the first row
    p = invoke(plot,
               Tuple{EpistemicNetworkAnalysis.AbstractENAModel{<:EpistemicNetworkAnalysis.AbstractLinearENARotation}},
               myENA;
               lims=lims,
               extraColors=sessionColors,
               leg=nothing,
               showCIs=false,
               showUnits=false,
            #    showNetworkLines=false,
               showTrajectoryBy=:SessionNum,
               groupBy=:SessionNum)
    savefig(p, "$(filename)_hairball.png")
end

println("Running gamuts...")
gamut("mr_pre_post", prePostMR, prePostFellowFilter, defaultColors, 1.1)
gamut("mr_divergent", activityTypeMR, fellowFilter, defaultColors, 1)
gamut("mcr_1_2", sessionMCR_1_2, fellowFilter, sessionColors, 1)
gamut("mcr_3_4", sessionMCR_3_4, fellowFilter, sessionColors, 1)
gamut("m2r_probe_toolkit", probeToolkitM2R, fellowFilter, defaultColors, 1)
gamut("m2r_toolkit_proto", toolkitPrototypeM2R, fellowFilter, defaultColors, 1)
gamut("m2r_proto_probe", prototypeProbeM2R, fellowFilter, defaultColors, 1)

println("Done!")

end # let