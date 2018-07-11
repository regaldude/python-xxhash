try:
    from xxhash.cpython import (xxh32, xxh32_digest, xxh32_intdigest,
                                                     xxh32_hexdigest,
                                xxh64, xxh64_digest, xxh64_intdigest,
                                                     xxh64_hexdigest,
                                XXHASH_VERSION)
except ImportError:
    from xxhash.cffi    import (xxh32, xxh32_digest, xxh32_intdigest,
                                                     xxh32_hexdigest,
                                xxh64, xxh64_digest, xxh64_intdigest,
                                                     xxh64_hexdigest,
                                XXHASH_VERSION)


VERSION = '1.1.0'
__all__ = ['xxh32', 'xxh32_digest', 'xxh32_intdigest', 'xxh32_hexdigest',
           'xxh64', 'xxh64_digest', 'xxh64_intdigest', 'xxh64_hexdigest',
           'VERSION', 'XXHASH_VERSION']
