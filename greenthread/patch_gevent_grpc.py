def patch_gevent_grpc():
    import gevent
    from gevent import monkey
    monkey.patch_all()
    import grpc.experimental.gevent as grpc_gevent
    grpc_gevent.init_gevent()
