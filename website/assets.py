from flask_assets import Bundle, Environment

def compile_statis_assets(app):
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False

    account_less_budle = Bundle(
        'src/less/account.less',
        filters = 'less,cssmin',
        output = 'dist/css/account.css',
        extra = {'rel': 'stylesheet/less'}
    )

    dashboard_less_budle = Bundle(
        "src/less/dashboard.less",
        filters="less,cssmin",
        output="dist/css/dashboard.css",
        extra={"rel": "stylesheet/less"},
    )

    js_bundle = Bundle('src/js/main.js', filters='jsmin', output="dist/js/main.js")

    assets.register('account_less_budle', account_less_budle)
    assets.register('dashboard_less_budle', dashboard_less_budle)
    assets.register('js_all', js_bundle)

    account_less_budle.build()
    dashboard_less_budle.build()
    js_bundle.build()