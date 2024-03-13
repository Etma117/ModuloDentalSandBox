const CACHE_NAME = 'dental-cache-' + new Date().getTime();

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll([
        '/offline/',
        '/',
        '/static/css/style.css',
        '/static/js/main.js',
        // Agrega aquí más recursos estáticos que desees cachear
      ]).catch((error) => {
        console.error('Error al agregar recursos al caché:', error);
      });
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).then((fetchResponse) => {
        // Cachear nuevos recursos durante la solicitud
        if (fetchResponse && fetchResponse.status === 200) {
          const responseToCache = fetchResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return fetchResponse;
      });
    }).catch(() => {
      // Si falla la solicitud y no hay caché disponible, devuelve una página de fallback offline
      if (event.request.mode === 'navigate') {
        return caches.match('/offline/');
      }
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (name !== CACHE_NAME) {
            return caches.delete(name);
          }
        })
      );
    })
  );
});

// Escucha el evento de conexión a Internet
self.addEventListener('online', (event) => {
  // Cuando se detecta una conexión, actualiza el caché con los datos más recientes
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return fetch('/actualizar-datos/')  // Ruta a la vista que actualiza los datos
          .then((response) => {
            return cache.put('/datos/', response); // Almacena la respuesta actualizada en el caché
          });
      })
  );
});
