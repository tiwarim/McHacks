import axios from "axios";

export const apiMethods = {
  getUsernames,
  getTweets
};

// this fnc returns whole bunch of users
async function getUsernames() {
  let config = { params: {q:data} }
  return await axios("https://api.twitter.com/1.1/users/search.json", config).then(
    response=>{return response.data}
    )
  
  };

// at this point, the parent knows the username and id of the child

// we use the id to get some past tweets of the child
async function getTweets(data) {
  let config = { params: { id: data} };
  return await axios("https://api.twitter.com/1.1/statuses/user_timeline.json", config).then(
    response=>{return response.data}
    )
}
