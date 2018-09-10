# -*- coding: utf-8 -*-
from flaskblog import app
# 68.231.144.153
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)