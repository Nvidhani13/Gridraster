#ifndef GRIDRASTER_GLOBAL_H
#define GRIDRASTER_GLOBAL_H

#include <QtGlobal>

#if defined(MYPLUGIN_LIBRARY)
#  define MYPLUGINSHARED_EXPORT Q_DECL_EXPORT
#else
#  define MYPLUGINSHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // GRIDRASTER_GLOBAL_H
