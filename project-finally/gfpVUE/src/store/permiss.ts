import { defineStore } from 'pinia';

interface ObjectList {
	[key: string]: string[];
}

// export const usePermissStore = defineStore('permiss', {
// 	state: () => {
// 		const keys = localStorage.getItem('ms_keys');
// 		return {
// 			key: keys ? JSON.parse(keys) : <string[]>[],
// 			defaultList: <ObjectList>{
// 				admin: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'],
// 				user: ['1', '2', '3', '11', '13', '14', '15']
// 			}
// 		};
// 	},
// 	actions: {
// 		handleSet(val: string[]) {
// 			this.key = val;
// 		}
// 	}
// });

  
export const usePermissStore = defineStore('permiss', {  
  state: () => {  
    const keys = localStorage.getItem('ms_keys');  
    let keyArray = [];  
    try {  
      if (keys) {  
        keyArray = JSON.parse(keys);  
      }  
    } catch (error) {  
      console.error('无法解析ms_keys为JSON:', error);  
      // 你可以选择清除localStorage中的ms_keys，或者保持为空数组  
      // localStorage.removeItem('ms_keys');  
    }  
      
    const defaultList: ObjectList = {  
      admin: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'],  
      user: ['1', '2', '3', '11', '13', '14', '15']  
    };  
      
    return {  
      key: keyArray,  
      defaultList  
    };  
  },  
  actions: {  
    handleSet(val: string[]) {  
      this.key = val;  
      localStorage.setItem('ms_keys', JSON.stringify(val));  
    }  
  }  
});
