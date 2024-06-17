const CACHE_NAME_DYNAMIC = 'dental-cache-dynamic-' + new Date().getTime();
const CACHE_NAME_STATIC = 'dental-cache--static-' + new Date().getTime();
const CACHE_NAME_INMUTABLE = 'dental-cache-inmutable' + new Date().getTime();

self.addEventListener('install', (event) => {
  event.waitUntil(
    Promise.all([

      // Cache estático -> App Shell
      caches.open(CACHE_NAME_STATIC).then((cache) => {
        return cache.addAll([
          '/offline/',
          '/',
          '/static/css/style.css',
          '/static/js/main.js'         
          // Agregar más recursos estáticos aquí para el funcionamiento de DentalDenters de forma Offline
        ]).catch((error) => {
          console.error('Error al agregar recursos estáticos al caché:', error);
        });
      }),

      // Cache inmutable
      caches.open(CACHE_NAME_INMUTABLE).then((cache) => {
        return cache.addAll([
          "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
          "https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback",  
          //<!-- Ionicons -->
          "https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css",
          "https://kit.fontawesome.com/78350df3d2.js",
          "https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css",
          "https://cdn.datatables.net/v/bs5/jq-3.7.0/jszip-3.10.1/dt-1.13.6/b-2.4.2/b-html5-2.4.2/b-print-2.4.2/datatables.min.css",
          'https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css',
          'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
          'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
          // Agregar recursos inmutables aquí
        ]).catch((error) => {
          console.error('Error al agregar recursos inmutables al caché:', error);
        });
      })
    ])
  );
});

 self.addEventListener('fetch', (event) => {
   event.respondWith(
     caches.match(event.request).then((response) => {
       if (response) {
         return response; // Si el recurso está en caché, devolverlo desde el caché
       } else {
         return fetch(event.request).then((fetchResponse) => {
           return caches.open(CACHE_NAME_DYNAMIC).then((cache) => {
             cache.put(event.request.url, fetchResponse.clone()); // Agregar el recurso al caché dinámico
             return fetchResponse; // Devolver el recurso desde la red
           });
         }).catch((error) => {
           console.error('Error al recuperar recurso desde la red:', error);
           // Aquí puedes devolver una página de error u otro recurso
         });
       }
     })
   );
 });



 self.addEventListener('fetch', (event) => {
   event.respondWith(
     caches.match(event.request).then((response) => {
       return response || fetchAndCache(event.request);
     })
   );
 });
 function fetchAndCache(request) {
   return fetch(request).then((fetchResponse) => {
     if (!fetchResponse || fetchResponse.status !== 200 || fetchResponse.type !== 'basic') {
       return fetchResponse;
     }

     const responseToCache = fetchResponse.clone();
     caches.open(CACHE_NAME).then((cache) => {
       cache.put(request, responseToCache);
     });

     return fetchResponse;
   }).catch((error) => {
     console.error('Error al recuperar la solicitud:', error);
     return caches.match('/offline/');
   });
 }

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (name !== CACHE_NAME_STATIC) {
            return caches.delete(name);
          }
        })
      );
    })
  );
});

self.addEventListener('sync', (event) => {
  if (event.tag === 'my-sync-tag') {
    event.waitUntil(
      getData().then((data) => {
        return sendDataToServer(data);
      }).then(() => {
        console.log('Sincronización completada');
      }).catch((error) => {
        console.error('Error en la sincronización:', error);
      })
    );
  }
});

function getData() {
  // Aquí obtienes los datos que deseas sincronizar
  return new Promise((resolve) => {
    // Simulación de obtener datos (puedes implementar tu lógica real aquí)
    setTimeout(() => {
      resolve({ exampleData: 'someData' });
    }, 2000); // Simula una demora en obtener datos
  });
}

function sendDataToServer(data) {
  // Aquí envías los datos al servidor
  return fetch('/api/sync', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

importScripts(
  'https://storage.googleapis.com/workbox-cdn/releases/6.5.4/workbox-sw.js'
);

self.addEventListener('push', (event) => {
  event.waitUntil(
    registration.showNotification("Hello!", {
      body: "This is a push notification!",
    })
  );
});

workbox.precaching.precacheAndRoute(self.__WB_MANIFEST || []);








// const CACHE_NAME = 'dental-cache-' + new Date().getTime();

// self.addEventListener('install', (event) => {
//   event.waitUntil(
//     caches.open(CACHE_NAME).then((cache) => {
//       return cache.addAll([
//         '/offline/',
//         '/',
//         '/static/css/style.css',
//         '/static/js/main.js'
//       ]).catch((error) => {
//         console.error('Error al agregar recursos al caché:', error);
//       });
//     })
//   );
// });

// self.addEventListener('fetch', (event) => {
//   event.respondWith(
//     caches.match(event.request).then((response) => {
//       return response || fetch(event.request).then((fetchResponse) => {
//         // Cachear nuevos recursos durante la solicitud
//         if (fetchResponse && fetchResponse.status === 200) {
//           const responseToCache = fetchResponse.clone();
//           caches.open(CACHE_NAME).then((cache) => {
//             cache.put(event.request, responseToCache);
//           });
//         }
//         return fetchResponse;
//       });
//     }).catch(() => {
//       // Si falla la solicitud y no hay caché disponible, devuelve una página de fallback offline
//       if (event.request.mode === 'navigate') {
//         return caches.match('/offline/');
//       }
//     })
//   );
// });

// self.addEventListener('activate', (event) => {
//   event.waitUntil(
//     caches.keys().then((cacheNames) => {
//       return Promise.all(
//         cacheNames.map((name) => {
//           if (name !== CACHE_NAME) {
//             return caches.delete(name);
//           }
//         })
//       );
//     })
//   );
// });

// // Escucha el evento de conexión a Internet
// self.addEventListener('online', (event) => {
//   // Cuando se detecta una conexión, actualiza el caché con los datos más recientes
//   event.waitUntil(
//     caches.open(CACHE_NAME)
//       .then((cache) => {
//         return fetch('/actualizar-datos/')  // Ruta a la vista que actualiza los datos
//           .then((response) => {
//             return cache.put('/datos/', response); // Almacena la respuesta actualizada en el caché
//           });
//       })
//   );
// });
