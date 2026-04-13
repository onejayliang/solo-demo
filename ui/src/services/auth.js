import api from './api';

export const AuthService = {
  login(credentials) {
    return api.post('/auth/login', credentials);
  },

  register(userData) {
    return api.post('/auth/register', userData);
  },

  logout() {
    return api.post('/auth/logout');
  },

  getProfile() {
    return api.get('/auth/profile');
  }
};
