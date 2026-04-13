import api from './api';

export const GenealogyService = {
  /**
   * 创建族谱
   * @param {Object} genealogy - 族谱信息
   * @returns {Promise<Object>} 创建结果
   */
  createGenealogy(genealogy) {
    return api.post('/genealogy/create', genealogy);
  },

  /**
   * 获取族谱列表
   * @returns {Promise<Object>} 族谱列表
   */
  getGenealogies() {
    return api.get('/genealogy/my');
  },

  /**
   * 获取族谱详情
   * @param {String} genealogyId - 族谱ID
   * @returns {Promise<Object>} 族谱详情
   */
  getGenealogyDetail(genealogyId) {
    return api.get(`/genealogy/${genealogyId}`);
  },

  /**
   * 更新族谱
   * @param {String} genealogyId - 族谱ID
   * @param {Object} genealogy - 更新数据
   * @returns {Promise<Object>} 更新结果
   */
  updateGenealogy(genealogyId, genealogy) {
    return api.put(`/genealogy/${genealogyId}`, genealogy);
  },

  /**
   * 删除族谱
   * @param {String} genealogyId - 族谱ID
   * @returns {Promise<Object>} 删除结果
   */
  deleteGenealogy(genealogyId) {
    return api.delete(`/genealogy/${genealogyId}`);
  },

  /**
   * 添加族员
   * @param {String} genealogyId - 族谱ID
   * @param {Object} member - 族员信息
   * @returns {Promise<Object>} 添加结果
   */
  addMember(genealogyId, member) {
    return api.post(`/genealogy/${genealogyId}/members`, member);
  },

  /**
   * 上传家族文献
   * @param {String} genealogyId - 族谱ID
   * @param {FormData} formData - 文献数据
   * @returns {Promise<Object>} 上传结果
   */
  uploadDocument(genealogyId, formData) {
    return api.post(`/genealogy/${genealogyId}/documents`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
  },

  /**
   * 设置族谱权限
   * @param {String} genealogyId - 族谱ID
   * @param {Object} permissions - 权限设置
   * @returns {Promise<Object>} 设置结果
   */
  setPermissions(genealogyId, permissions) {
    return api.put(`/genealogy/${genealogyId}/permissions`, permissions);
  }
};
