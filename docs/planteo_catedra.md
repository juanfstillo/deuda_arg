# Planteo para Cátedra

## 1. Pregunta y gancho

**¿A quién protege el diseño regulatorio del crédito en Argentina: al sistema financiero o al deudor?**

Gancho para abrir la presentación: en paralelo a un régimen de mora en máximos históricos (16,4% en préstamos personales bancarios a jun-2026; refinanciaciones sobre stock de crédito a familias en el nivel más alto de la serie BCRA desde 2010), el BCRA **eliminó** el tope a la tasa de refinanciamiento de saldos de tarjeta (Com. "A" 8026, may-2024) mientras sostenía durante más de un año un instrumento de fondeo remunerado —las LEFIs— **exclusivo para bancos**, sin equivalente para fintech. La paradoja a explicar: el diseño regulatorio se volvió *menos* protector del deudor justo cuando la mora subía, mientras preservaba canales de privilegio para una parte del sistema financiero. Eso es lo que hay que explicar — y "el mercado lo pedía" no alcanza como explicación, porque es exactamente lo que predeciría la teoría de captura.

## 2. Los tres mecanismos, aplicados uno por uno

No usar los tres marcos como decoración simultánea. Cada uno explica un fenómeno distinto y compite con los otros por evidencia — la presentación gana si mostramos cuál mecanismo explica mejor cuál pieza del diseño regulatorio.

### 2.1 Captura regulatoria (Stigler, Peltzman)
**Predicción:** la regulación termina sirviendo al interés del regulado (bancos/fintech) antes que al interés difuso del público (deudores).

**Dónde buscarla:** en la *eliminación del tope de tasa de refinanciamiento de tarjeta* (Comunicación "A" 8026, BCRA, anunciada 24/05/2024, vigente desde jun-2024 — reemplazó un tope de 122% TNA para refinanciar saldos de hasta $200.000). Preguntas a responder con datos:
- ¿Qué pasó con la tasa efectiva de refinanciamiento antes/después de A 8026? (serie BCRA, tasas activas)
- ¿A quién benefició en el margen: bancos grandes, fintech, o ambos por igual? (la asimetría regulatoria bancos/fintech sugiere que no es un favor parejo — hay que ver si el diseño post-2024 iguala o profundiza esa asimetría)

### 2.2 Asimetría bancos/fintech, vía las LEFIs (Stigler/Peltzman también aplica acá)
**Corrección:** lo que en el README decía "fin de REFIS" es en realidad **LEFIs (Letras Fiscales de Liquidez)** — títulos de deuda emitidos por el Tesoro desde 2024 para absorber los pesos excedentes de los bancos y trasladar los pasivos remunerados del BCRA al Tesoro (saneamiento de balance, "emisión cero"). No tiene nada que ver con refinanciación de deudas de consumidores — es arquitectura de liquidez mayorista entre el Banco Central/Tesoro y las entidades financieras.

**Por qué igual importa para la pregunta de investigación:** las LEFIs **solo podían suscribirse y negociarse entre el BCRA y los bancos** — no fintechs, no otros proveedores de crédito. Es evidencia directa y concreta de la asimetría regulatoria bancos/fintech que el README ya señalaba como sub-tema aparte: durante 2024–2025 los bancos tuvieron acceso a un instrumento remunerado, respaldado por el Tesoro, que las fintech nunca tuvieron. Cronología:
- 2024: se eliminan los pases pasivos (Leliq) y la deuda remunerada del BCRA se traslada a LEFIs emitidas por el Tesoro, en manos exclusivamente de bancos.
- 10/07/2025: el BCRA deja de ofrecer LEFIs a las entidades; vencimiento final 17/07/2025. El stock se canjea por LECAPs/BONCAPs (instrumentos de mercado, no exclusivos de bancos) y el Central pasa a manejar liquidez con encajes y operaciones de mercado abierto — el paso final de la "Fase 2/3" del esquema monetario.

Esto es más útil como evidencia de **asimetría estructural** (una entidad tiene acceso a un canal de fondeo/backstop que la otra no) que como un caso de blame avoidance — no hay ahí un intento de esquivar responsabilidad política, es diseño de arquitectura monetaria. Vale la pena mantenerlo separado de 2.1 en la presentación aunque ambos sean "captura", porque la mecánica es distinta: 2.1 es una tasa que sube para el deudor final; esto es un privilegio de fondeo para el banco.

### 2.3 Blame avoidance / framing de responsabilidad (Weaver)
**Predicción:** el regulador no busca maximizar bienestar ni necesariamente favorecer al capturado — busca minimizar su propia exposición política ante un resultado negativo, aunque eso signifique inacción o transferencia de responsabilidad.

**Dónde buscarla:** en el discurso oficial más que en una norma puntual — la nota de agosto 2026 donde el BCRA publicó "consejos para quienes toman un préstamo" es un caso de manual: reframing de responsabilidad hacia el deudor individual ("tomá decisiones informadas") publicado en medio del debate público por la mora récord, sin que eso implique un cambio de norma que le cueste algo al sistema financiero. **Pendiente:** buscar 1-2 casos más de este tipo de comunicación (notas de prensa del BCRA, no solo comunicaciones normativas) para que no quede como un caso único.

### 2.4 Policy feedback
**Predicción:** el diseño regulatorio pasado cambia las expectativas y el comportamiento futuro de deudores y entidades, generando una trayectoria que se retroalimenta (no es un evento aislado sino una secuencia).

**Dónde buscarla:** en la secuencia 2024→2025→2026: fin de Leliq/pases pasivos → LEFIs como puente → fin de LEFIs (jul-2025) → bancos pasan a gestionar liquidez con encajes más altos y mercado secundario (LECAP/BONCAP) → posible traslado a costo de fondeo y por ende a tasas activas → efecto sobre cuotas y mora. En paralelo, el salto de refinanciaciones voluntarias sobre stock de crédito a familias (3,2% vs. 1,6% seis meses antes, según prensa sobre series BCRA) coincide en el tiempo con este reacomodamiento de liquidez bancaria. La pregunta empírica: ¿el salto de refinanciaciones responde al fin de las LEFIs (canal de costo de fondeo) o es independiente (pura dinámica de ingresos/inflación, ver sección 3)? Esto requiere cruzar la serie de tasas activas con la fecha jul-2025 para ver si hay quiebre.

## 3. Hipótesis rival a descartar

Antes de adjudicar el patrón al diseño regulatorio, hay que descartar la explicación puramente macroeconómica: **la mora sube por inflación/licuación de ingresos reales y volatilidad cambiaria, independientemente de cómo esté diseñada la regulación.** Si la serie de mora se mueve en lockstep con inflación/salario real y el timing de los cambios regulatorios no coincide con quiebres en la serie de mora, el argumento "diseño regulatorio" se debilita. Esto es lo que va a resolver el cruce con EPH (deuda/ingreso) de la sub-pregunta 1 — es el control, no un tema aparte.

## 4. De la pregunta a los datos (mapeo explícito)

| Sub-pregunta README | Qué necesito para responderla | Estado |
|---|---|---|
| 1. ¿Por qué se endeudan los hogares? | Serie deuda/ingreso 2023–hoy (BCRA tasas + INDEC/EPH ingreso) | Pendiente — notebook 03 |
| 2. ¿Por qué no pagan? (mora por entidad/segmento) | Anexo estadístico Informe sobre Bancos (mora por entidad, cartera consumo/comercial) — **no está en la API**, se descarga a mano | Pendiente — descarga manual |
| 3. ¿Protege al sistema o al deudor? | Timeline BCRA (Com. "A" 8026 + cronología LEFIs 2024→jul-2025) cruzado con series de tasas activas y mora | Fechas confirmadas — falta el cruce cuantitativo con las series |

## 5. Qué falta verificar antes de dar esto por cerrado

- [x] ~~Confirmar comunicación y fecha del fin de "REFIS"~~ — corregido: es LEFIs, no REFIS. Cronología confirmada: creación 2024 (sustituyen pases pasivos/Leliq), BCRA deja de ofrecerlas 10/07/2025, vencimiento 17/07/2025, canje por LECAPs/BONCAPs.
- [ ] Confirmar si hay quiebre visible en la serie de tasas activas/BADLAR alrededor de jul-2025 (fin de LEFIs) — necesario para sostener el argumento de policy feedback de la sección 2.4.
- [ ] Buscar 1-2 ejemplos más de comunicación oficial tipo "consejos para tomar un préstamo" (sección 2.3) para no apoyar blame avoidance en un solo caso.
- [ ] Confirmar si existe asimetría normativa explícita bancos vs. fintech más allá de las LEFIs (ej. en Com. "A" 8026 o en el régimen de encajes post-LEFI) — o si la asimetría es solo de facto por alcance de supervisión.

## 6. Estructura tentativa de la presentación

1. Gancho (paradoja: mora récord + desregulación, sección 1)
2. Pregunta y sub-preguntas
3. Marco teórico — los tres mecanismos y qué predice cada uno (sección 2)
4. Evidencia — timeline regulatorio + series (tasas, mora, deuda/ingreso)
5. Descarte de la hipótesis macro pura (sección 3)
6. Conclusión: qué mecanismo explica qué pieza, y qué queda abierto
7. Próximos pasos / escalado a ponencia
