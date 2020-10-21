const axios = require('axios').default
const BaseDriver = require('./BaseDriver')


module.exports = class LandingJobs extends BaseDriver {

    constructor() {
        super()
    }

    url = 'https://landing.jobs/api/v1/jobs';

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
            console.info("Fetching jobs from LandingJobs")
            //nothing to do here
            if (this.config.tags.length === 0) {
                console.info("No tags defined in " + this.configFileName())
                console.info("Returning empty array...")
                return []
            }


            let allJobs = []
            let limit = 50 // limit per request, api imposed
            for (let page = 0; page < 10000; page++) {

                let payload = {
                    'limit': limit,
                    'offset': page * limit
                }

                console.info('Fetching ' + limit)
                let jobs = await axios.get(this.url, {
                    params: payload
                })

                if (jobs.data.length === 0) {
                    break;
                } else {
                    allJobs = allJobs.concat(jobs.data)
                }
            }
            console.info('Filtering ...')
            let filteredJobs = allJobs.filter(x => this.filterByTags(x.tags) && this.filterUnpublished(x.id))

            console.info(filteredJobs.length + ' jobs found ...')

            console.info('Mapping and sorting ...')

            return filteredJobs.map(x => {
                return {
                    id: x.id,
                    url: x.url
                }
            }).sort(x => x.id)
        } catch (error) {
            console.error("LandingJobs -> getJobs -> error", error)

        }
    }

    /**
     * Filters jobs using an array of relevant tags
     * @param {array} tags 
     */
    filterByTags(tags) {
        try {
            for (let index = 0; index < tags.length; index++) {
                if (this.config.tags.map(x => x.toUpperCase()).indexOf(tags[index].toUpperCase()) > -1) {
                    return true
                }
            }
            return false;
        } catch (error) {
            console.error("LandingJobs -> filterByTags -> error", error)

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
            console.error("LandingJobs -> storePublishedJob -> error", error)
        }
    }
}