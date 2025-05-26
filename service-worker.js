
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('livraria-cache').then(cache => {
            return cache.addAll([
                '/index.html',
                '/static/css/styles.css',
                '/static/js/main.js',
                '/manifest.json'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
