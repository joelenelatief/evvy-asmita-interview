import axios from 'axios';

const BASE_URL = `http://localhost:8001`;

const getRequest = (url, successCallback, errorCallback) => {
  return axios.get(BASE_URL + url)
    .then(response => { if (successCallback) { return successCallback(response); } })
    .catch((error) => { if (errorCallback) { return errorCallback(error); } });
};

const postRequest = (url, data, successCallback, errorCallback) => {
  return axios.post(BASE_URL + url, data)
    .then((response) => { if (successCallback) { return successCallback(response); } })
    .catch((error) => { if (errorCallback) { return errorCallback(error); } });
};

export { getRequest, postRequest }
