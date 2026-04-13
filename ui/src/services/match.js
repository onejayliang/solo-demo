import api from './api';

export const MatchService = {
  /**
   * 获取匹配结果
   * @param {String} dataId - 资料ID
   * @returns {Promise<Object>} 匹配结果
   */
  getMatches(dataId) {
    return api.get(`/match/relatives/${dataId}`);
  },

  /**
   * 提交认祖申请
   * @param {Object} application - 申请信息
   * @returns {Promise<Object>} 申请结果
   */
  submitApplication(application) {
    return api.post('/application/submit', application);
  },

  /**
   * 获取申请列表
   * @returns {Promise<Object>} 申请列表
   */
  getApplications() {
    return api.get('/application/my');
  },

  /**
   * 获取申请详情
   * @param {String} applicationId - 申请ID
   * @returns {Promise<Object>} 申请详情
   */
  getApplicationDetail(applicationId) {
    return api.get(`/application/${applicationId}`);
  },

  /**
   * 生成表字
   * @param {Object} data - 个人信息
   * @returns {Promise<Object>} 表字结果
   */
  generateStyleName(data) {
    return api.post('/match/generate-style-name', data);
  }
};
