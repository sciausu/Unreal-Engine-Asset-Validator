# Below is the command to run the program in the Command Terminal / Console / CMD
# "<Enter Path to file>\UnrealEditor-Cmd.exe" "<Enter Path to file>.uproject" -run=pythonscript -script="<Enter Path to file>\assetValidator.py" -stdout -FullStdOutLogOutput

# Naming conventions used as reference
# https://dev.epicgames.com/documentation/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects

import unreal

UETypes = {
    # Note: Key names will be merged as to match the result from the asset registry
    # Additional names and conventions can be added to the users discretion

    # General
    "StaticMesh" : "SM_",
    "HDRI" : "HDR_",
    "Material" : "M_",
    "MaterialInstance" : "MI_",
    "PhysicsAsset" : "PHYS_",
    "PhysicsMaterial" : "PM_",
    "PostProcessMaterial" : "PPM_",
    "SkeletalMesh" : "SK_",
    "Texture" : "T_",
    "Texture2D" : "T_",
    "OCIOProfile" : "OCIO_",
    
    # Blueprints
    "ActorComponent" : "AC_",
    "AnimationBlueprint" : "ABP_",
    "BlueprintInterface" : "BI_",
    "Blueprint" : "BP_",
    "CurveTable" : "CT_",
    "DataTable" : "DT_",
    "Enum" : "E_",
    "Structure" : "F_",
    "WidgetBlueprint" : "WBP_",
    
    # Particle Effects
    "NiagaraEmitter" : "FXE_",
    "NiagaraSystem" : "FXS_",
    "NiagaraFunction" : "FXF_",
    
    # Skeletal Mesh Animation
    "Rig" : "Rig_",
    "Skeleton" : "SKEL_",
    "Montages" : "AM_",
    "AnimationSequence" : "AS_",
    "BlendSpace" : "BS_",
    
    # ICVFX
    "NDisplayConfiguration" : "NDC_",
    
    # Animation
    "LevelSequence" : "LS_",
    "SequencerEdits" : "EDIT_",
    
    # Media
    "MediaSource" : "MS_",
    "MediaOutput" : "MO_",
    "MediaPlayer" : "MP_",
    "MediaProfile" : "MPR_",
    
    # Other
    "LevelSnapshots" : "SNAP_",
    "RemoteControlPreset" : "RCP_",
}


def main():
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    allAssets = registry.get_all_assets()

    namingIssues = []
    missingDepends = []


    for asset in allAssets:
        Atype = str(asset.asset_class_path.asset_name)

        if Atype in UETypes and str(asset.package_path)[0:5] == "/Game":
            prefix = UETypes[Atype]

            if str(asset.asset_name)[0:len(prefix)] != prefix:
                namingIssues.append([prefix, str(asset.asset_name)])
    
    print("Files with naming convention issues: ")

    for file in namingIssues:
        print(file[1], "-->", file[0]+file[1])

    print()
        


if __name__ ==  "__main__":
    main()

