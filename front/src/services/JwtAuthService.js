import fetch from 'auth/FetchInterceptor';

const JwtAuthService = {};

JwtAuthService.login = function (data) {
  return fetch({
    url: `${process.env.REACT_APP_PROTOCOL}${process.env.REACT_APP_HOST}user/login`,
    method: 'post',
    headers: {
      'public-request': 'true',
    },
    data: data,
  });
};

JwtAuthService.signUp = function (data) {
  return fetch({
    url: '/posts',
    method: 'post',
    headers: {
      'public-request': 'true',
    },
    data: data,
  });
};

export default JwtAuthService;
