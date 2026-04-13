import api from './api';

export const AncestorDataService = {
  /**
   * 提交祖上资料
   * @param {Object} data - 祖上资料
   * @returns {Promise<Object>} 提交结果
   */
  submitData(data) {
    return api.post('/ancestor-data/submit', data);
  },

  /**
   * 获取祖上资料列表
   * @returns {Promise<Object>} 资料列表
   */
  getMyData() {
    return api.get('/ancestor-data/my');
  },

  /**
   * 获取资料详情
   * @param {String} dataId - 资料ID
   * @returns {Promise<Object>} 资料详情
   */
  getDataDetail(dataId) {
    return api.get(`/ancestor-data/${dataId}`);
  },

  /**
   * 更新资料
   * @param {String} dataId - 资料ID
   * @param {Object} data - 更新数据
   * @returns {Promise<Object>} 更新结果
   */
  updateData(dataId, data) {
    return api.put(`/ancestor-data/${dataId}`, data);
  },

  /**
   * 删除资料
   * @param {String} dataId - 资料ID
   * @returns {Promise<Object>} 删除结果
   */
  deleteData(dataId) {
    return api.delete(`/ancestor-data/${dataId}`);
  }
};
