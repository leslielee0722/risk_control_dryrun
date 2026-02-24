from livereload import Server, shell

server = Server()
server.watch('*.html')
server.watch('**/*.html')
server.watch('**/*.css')
server.watch('**/*.js')
server.serve(port=9090, host='0.0.0.0', open_url_delay=None)
