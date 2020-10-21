const axios = require('axios').default
const BaseDriver = require('./BaseDriver')
require('dotenv').config()

module.exports = class ItJobs extends BaseDriver {

    constructor() {
        this.url = 'https://api.itjobs.pt/job/search.json';
        super()
    }

    /**
     * @returns the default config
     */
    defaultConfig() {
        return {
            tags: [],
            last_published_id: 0
        }
    }

    //     * @returns {[{id:number, url:string}], ...} array of job objects, sorted by id
    /**
     * Retrieves jobs from the api
     */
    async getJobs() {
        try {
            console.info("Fetching jobs from ItJobs")
            //nothing to do here
            if (this.config.tags.length === 0) {
                console.info("No tags defined in " + this.configFileName())
                console.info("Returning empty array...")
                return []
            }


            let allJobs = []
            let limit = 10 // limit per request, api imposed
            let tagsList = this.config.tags.length;

            for (let tagConfig = 0; tagConfig < tagsList; tagConfig++) {
                for (let page = 0; page < 1; page++) {
                    console.info('tagConfig ' + this.config.tags[tagConfig])

                    let payload = {
                        'api_key': process.env.TOKEN_ITJOBS,
                        'limit': limit,
                        'q': this.config.tags[tagConfig],
                        'offset': page * limit
                    }

                    let jobs = await axios.get(this.url, {
                        params: payload
                    });

                    if (jobs.data.results.length === 0) {
                        break;
                    } else {
                        allJobs = allJobs.concat(jobs.data.results)
                    }
                }
            }

            console.info('Filtering ...')
            let filteredJobs = allJobs.filter(x => this.filterUnpublished(x.id))


            console.info(filteredJobs.length + ' jobs found ...')

            console.info('Mapping and sorting ...')

            return filteredJobs.map(x => {
                return {
                    id: x.id,
                    url: "https://www.itjobs.pt/oferta/" + x.id + "/" + x.slug

                }
            }).sort(x => x.id)
        } catch (error) {
            console.error("LandingJobs -> getJobs -> error", error)
        }
    }


    /**
     * Filter jobs by job id
     * @param {number} id the job id
     */
    filterUnpublished(id) {
        return parseInt(id) > this.config.last_published_job_id
    }


    storePublishedJob(job) {
        try {
            console.info("Storing job id " + job.id)
            this.config.last_published_job_id = job.id
            this.storeConfig()
        } catch (error) {
            console.error("ItJobs -> storePublishedJob -> error", error)
        }
    }
}