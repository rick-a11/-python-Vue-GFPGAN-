import { registerAction } from 'echarts';
import request from '../utils/request';
import axios  from '../utils/request';

import base from "./base"
import Login from '../views/login.vue';

const api = {


}

export const fetchData = () => {
    return request({
        url: './table.json',
        method: 'get'
    });
};

export default api;