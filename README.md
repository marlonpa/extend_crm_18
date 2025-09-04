==========================
Módulo Extend CRM (Odoo 18)
==========================

Descripción
===========

Este módulo extiende la funcionalidad estándar de **CRM Leads** en Odoo, 
añadiendo campos personalizados y procesos de negocio para una mejor gestión 
de oportunidades y seguimiento comercial.

Características principales
===========================

- **Nuevos campos en crm.lead**:
  
  * Categoría del lead (Residencial, Empresarial, Gubernamental).
  * Fecha límite de entrega.
  * Fecha de aprobación.
  * Usuario que aprobó el lead.
  * Duración (en horas) transcurrida desde la aprobación.
  * Indicador de instalación postventa (con fecha asociada).
  * Número de contrato de referencia.
  * Requerimiento de soporte postventa.

- **Botón de aprobación**:
  
  * Permite registrar la fecha de aprobación y el usuario aprobador.

- **Campo calculado**:
  
  * Cálculo automático del tiempo transcurrido desde la aprobación hasta la fecha actual.
  * Persistido en base de datos y actualizado por un **cron job**.

- **Chatter integrado**:
  
  * Seguimiento de cambios con `tracking=True`.
  * Soporte para seguidores, actividades y mensajes en cada lead.

- **Datos iniciales de ejemplo**:
  
  * Se incluyen dos **partners demo** y dos **leads demo** preconfigurados, 
    para validar el comportamiento del módulo en un entorno nuevo.

Requisitos
==========

- Odoo 18.0 (Community o Enterprise).
- Módulo base **CRM** (`crm`).

Instalación
===========

1. Copiar el módulo en la carpeta de addons:

   .. code-block:: bash

      cp -r extend_crm /mnt/extra-addons/

2. Actualizar la lista de aplicaciones en Odoo.

3. Instalar el módulo **==========================
Módulo Extend CRM (Odoo 18)
==========================

Descripción
===========

Este módulo extiende la funcionalidad estándar de **CRM Leads** en Odoo, 
añadiendo campos personalizados y procesos de negocio para una mejor gestión 
de oportunidades y seguimiento comercial.

Características principales
===========================

- **Nuevos campos en crm.lead**:
  
  * Categoría del lead (Residencial, Empresarial, Gubernamental).
  * Fecha límite de entrega.
  * Fecha de aprobación.
  * Usuario que aprobó el lead.
  * Duración (en horas) transcurrida desde la aprobación.
  * Indicador de instalación postventa (con fecha asociada).
  * Número de contrato de referencia.
  * Requerimiento de soporte postventa.

- **Botón de aprobación**:
  
  * Permite registrar la fecha de aprobación y el usuario aprobador.

- **Campo calculado**:
  
  * Cálculo automático del tiempo transcurrido desde la aprobación hasta la fecha actual.
  * Persistido en base de datos y actualizado por un **cron job**.

- **Chatter integrado**:
  
  * Seguimiento de cambios con `tracking=True`.
  * Soporte para seguidores, actividades y mensajes en cada lead.

- **Datos iniciales de ejemplo**:
  
  * Se incluyen dos **partners demo** y dos **leads demo** preconfigurados, 
    para validar el comportamiento del módulo en un entorno nuevo.

Requisitos
==========

- Odoo 18.0 (Community o Enterprise).
- Módulo base **CRM** (`crm`).

Instalación
===========

1. Copiar el módulo en la carpeta de addons:

   .. code-block:: bash

      cp -r extend_crm /mnt/extra-addons/

2. Actualizar la lista de aplicaciones en Odoo.

3. Instalar el módulo **Extend CRM** desde el backend o mediante terminal:

   .. code-block:: bash

      ./odoo-bin -d <nombre_base> -i extend_crm

Uso
===

1. Ingresar al menú **CRM → Leads** o **CRM → Oportunidades**.
2. Crear un nuevo lead y completar los campos adicionales definidos.
3. Usar el **botón de aprobación** para marcar la fecha y usuario aprobador.
4. Verificar el cálculo automático del tiempo transcurrido desde la aprobación.
5. Revisar el chatter para el seguimiento de cambios.

Archivos incluidos
==================

- **models/**: definición de los campos heredados.
- **views/**: personalización de la vista `crm.lead.form`.
- **data/**:
  
  * `cron_compute_since_approved.xml`: tarea programada para actualizar las horas transcurridas.
  * `demo_data.xml`: partners y leads de ejemplo.

Mantenimiento
=============

- Autor: Tu Nombre
- Email: tu.email@dominio.com
- Licencia: LGPL-3
- Estado: Desarrollo / Producción (ajustar según corresponda)

** desde el backend o mediante terminal:

   .. code-block:: bash

      ./odoo-bin -d <nombre_base> -i extend_crm

Uso
===

1. Ingresar al menú **CRM → Leads**.
2. Crear un nuevo lead y completar los campos adicionales definidos.
3. Usar el botón de **aprobar** para marcar la fecha y usuario aprobador.
4. Verificar el cálculo automático del tiempo transcurrido desde la aprobación.
5. Revisar el chatter para el seguimiento de cambios.

Archivos incluidos
==================

- **models/**: definición de los campos heredados.
- **views/**: personalización de la vista `crm.lead.form`.
- **data/**:
  
  * `cron_compute_since_approved.xml`: tarea programada para actualizar las horas transcurridas.
  * `demo_data.xml`: partners y leads de ejemplo.

Mantenimiento
=============

- Autor: Tu Nombre
- Email: ingmarlonpal@gmail.com
- Licencia: LGPL-3
- Estado: Desarrollo / Producción (ajustar según corresponda)


