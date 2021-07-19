import axios from "axios"
//ChangedBy  ZHJ
// 服务器的URL
const SERVICE_ROOT = "http://localhost:8080/data/";

// 创建axios对象
const service = axios.create({
    timeout: 5000,
});

// 封装HTTP请求 ("post", "users.json", FormData)
export const requestData = (request_method, request_url, request_data)=>{
    // var response = service();
    // return response;

    return  service({
        url: SERVICE_ROOT + request_url,
        method: request_method,
        params: request_data
    });
}

