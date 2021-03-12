import web

urls = (
    '/', 'api.Api',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
