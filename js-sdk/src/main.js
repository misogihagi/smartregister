import lib from './lib'
let hostName = null;
let authHostName = null;
const debug = true
class Bandoor {
  constructor(cfg) {
    smrg_access_key_id
    smrg_secret_access_key
    this.cfg.origin = cfg
    this.cfg.endpoint = debug ? 'http://localhost:8000' : cfg.development ? "" : ""
    this.cfg.contractId = cfg.contractId
  }
  async init() {
    this.auth = await this.authentication(this.cfg)
  }
  async authentication(cfg) {
    const res = await lib.fetch(`${cfg.endpoint}/app/${cfg.contractId}/token`, {
      method: 'post',
      headers: {
        "Authorization": "Basic " + lib.btoa([cfg.clientId, cfg.clientSecret].join(":")),
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: JSON.stringify({
        "grant_type": "client_credentials",
        "scope": cfg.scope || cfg.scopes.join(" "),
      })
    });
    if (res.status !== 200) {
      throw new Error("AuthenticationFailed");
    }
    this.cfg.accessToken = JSON.parse(await res.json())['access_token']
  }
  listMenu() {
    if (!this.auth) throw new Error("Not Authenticated");
    return this.callAPI('list_menu', 'GET')
  }
}
const api_call = async(path, method, data = {}) => {
  const full_path = `{this.cfg.endpoint}/${this.cfg.contractId}/` + path;
  const options = {
    method,
    headers: {
      'Authorization': 'Bearer ' + access_token,
      'Content-Type': "application/json",
      'Accept': "application/json",
    }
  }
  if (method === "GET") {
    options.qs = JSON.stringify(data);
  } else {
    options.body = JSON.stringify(data);
  }
  return await lib.fetch(full_path, options).then(d => {
    return d.json()
  })
}