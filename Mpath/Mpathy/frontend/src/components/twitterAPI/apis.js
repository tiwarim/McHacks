import axios from "axios";

export const apiMethods = {
  getTestDataNoParams,
  getTestDataWithParams
};

async function getTestDataNoParams() {
  return await axios("https://swapi.co/api/planets/8/").then(response => {
    return response.data;
  });
}

// data has 2 params name, id
async function getTestDataWithParams(data) {
  let config = { params: { name: data.name, id: data.id } };

  return await axios("https://swapi.co/api/planets/8/", config);
}
