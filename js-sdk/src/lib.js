import fetch from 'node-fetch';
const lib={}
function btoa(string) {
	  if (process.browser) {
		      return btoa(string);
		    } else {
			        return Buffer.from(string, 'binary').toString('base64');
			     }
}
lib.btoa=btoa
function libfetch(string) {
	          if (process.browser) {
			                        return fetch;
			                      } else {
						                                      return nodefetch;
						                                   }
}
lib.fetch=libfetch

export default lib
