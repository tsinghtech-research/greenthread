def monkey_patch():
    import os
    backend = os.environ.get('GREEN_BACKEND', 'eventlet').lower()
    if backend == 'eventlet':
        import eventlet
        eventlet.monkey_patch()
    elif backend == 'gevent':
        import gevent.monkey
        gevent.monkey.patch_all()
    else:
        raise RuntimeError(f"invalid backend found! {backend}")
