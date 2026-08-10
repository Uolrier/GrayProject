import workspaceConfig from "../config/workspace.json";


export function loadWorkspaceConfig(){

    return workspaceConfig;

}


export function getPanelConfig(id){

    const config = loadWorkspaceConfig();


    return config.panels.find(
        panel => panel.id === id
    );

}