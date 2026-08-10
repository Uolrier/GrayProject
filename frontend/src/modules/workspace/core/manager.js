import {
    loadWorkspace,
    loadTheme
} from "./loader";


class WorkspaceManager {


    constructor(){

        this.workspace = loadWorkspace();

        this.theme = loadTheme();

    }


    getWorkspace(){

        return this.workspace;

    }


    getTheme(){

        return this.theme;

    }


}


export default new WorkspaceManager();