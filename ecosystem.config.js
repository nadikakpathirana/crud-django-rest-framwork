module.exports = {
  apps : [{
    name: 'uiuxpoc',
    cmd: 'manage.py',
    args: 'runserver 0.0.0.0:8082',
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      ENV: 'development'
    },
    env_production : {
      ENV: 'production'
    }
  }, {
    name: 'uiuxpoc',
    cmd: 'manage.py',
    interpreter: 'python3'
  }]
};
