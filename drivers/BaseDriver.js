const {
    rejects
} = require('assert');
const fs = require('fs');

module.exports = class BaseDriver {

    config = {}
    constructor() {
        this.readConfig()
    }

    configFileName() {
        return this.constructor.name + '.json'
    }

    /**
     * 
     * @return {[{id:number, url:string}, ...]}  array of job objects
     */

    async getJobs() {
        throw "Not implemented!"
    }

    /**
     * @returns the default config
     */
    defaultConfig() {
        throw "Not implemented!"
    }

    /**
     * Stores the configuration
     */
    storeConfig() {
        try {
            fs.writeFileSync(this.configFileName(), JSON.stringify(this.config))
        } catch (error) {
            console.error("LandingJobs -> storeConfig -> error", error)
        }
    }

    /**
     * Stores the id of the last published job
     * Jobs should be publish by id sequence
     * @param {{id:number, url:string}} job job object 
     */
    storePublishedJob(job) {
        throw "Not implemented!"
    }
    readConfig() {
        try {
            if (!fs.existsSync(this.configFileName())) {
                this.config = this.defaultConfig()
                this.storeConfig()
            } else {
                this.config = JSON.parse(fs.readFileSync(this.configFileName()))
            }

        } catch (error) {
            console.error("BaseDriver -> readConfig -> error", error)
        }
    }

}