# Marco Teórico

Este documento desarrolla en profundidad los tres cuerpos teóricos que estructuran el análisis del proyecto, sintetizados de forma aplicada en `planteo_catedra.md`. El objetivo no es usarlos como "decoración simultánea", sino como hipótesis rivales/complementarias que compiten por explicar piezas distintas del mismo fenómeno: el diseño regulatorio del crédito en Argentina entre 2023 y 2026.

## 1. Captura regulatoria (Stigler, 1971; Peltzman, 1976)

### 1.1 El planteo original de Stigler

George Stigler abrió en 1971, con "The Theory of Economic Regulation" (*Bell Journal of Economics and Management Science*, 2(1), 3-21), lo que se conoció como la "teoría económica de la regulación" o teoría de la captura. Stigler partió de una pregunta distinta a la que dominaba el campo hasta entonces: en lugar de preguntar qué efectos tiene la regulación, preguntó por sus causas. Su hipótesis central fue que la regulación no surge para corregir fallas de mercado en beneficio del interés público difuso, sino que, como regla general, es adquirida por la propia industria regulada y diseñada y operada primariamente para su beneficio. La lógica subyacente es de acción colectiva: los grupos concentrados (productores, entidades financieras) tienen incentivos y capacidad organizativa para lobbiar por regulación favorable, mientras que los consumidores, con intereses difusos y costos de organización más altos, rara vez logran contrapesarlos. Stigler nunca usó literalmente el término "regulatory capture" en el artículo, pero es la referencia obligada de la que deriva toda la literatura posterior sobre el tema.

### 1.2 La extensión de Peltzman

Sam Peltzman, en "Toward a More General Theory of Regulation" (*Journal of Law and Economics*, 19(2), 211-240, 1976), reformuló el modelo de Stigler para resolver una limitación importante: la versión original no explicaba por qué a veces el Congreso (o el regulador) sanciona normas que perjudican a la industria, ni por qué la protección regulatoria varía en intensidad. Peltzman reemplazó la figura abstracta del "regulador" por la de un actor político (legislador) que maximiza apoyo político/electoral, no bienestar social ni beneficio sectorial puro. El regulador pondera, en un equilibrio, cuánto puede favorecer al sector regulado sin perder el respaldo del público general — de ahí que la protección al productor tienda a ser mayor en recesiones y menor en expansiones, según Peltzman. Esta reformulación es la que habilita a pensar la captura no como un resultado binario (capturado / no capturado) sino como un punto de equilibrio que se mueve con el contexto político y macroeconómico.

### 1.3 Aplicación al caso: dos mecanismos distintos, no uno solo

El proyecto usa esta familia teórica en dos lugares que conviene no confundir:

- **Eliminación del tope a la tasa de refinanciamiento de tarjeta** (Comunicación "A" 8026, BCRA, may-2024): esto es captura en el sentido estricto de Stigler/Peltzman — una norma que remueve un límite protector al deudor final, en el momento en que la mora ya mostraba tensión. La pregunta empírica es si la tasa efectiva de refinanciamiento se movió después de la norma, y a favor de qué actores (bancos grandes, fintech, o ambos).
- **Asimetría bancos/fintech vía las LEFIs (2024-jul. 2025)**: es captura en un sentido más estructural — no una tasa que sube para el deudor, sino un canal de fondeo remunerado y respaldado por el Tesoro al que solo los bancos tuvieron acceso. Conviene tratarlo como una variante distinta dentro del mismo marco (privilegio de acceso a un mercado, no extracción directa de renta al consumidor), siguiendo la lógica de Peltzman de que la protección regulatoria no es pareja entre todos los actores regulados sino que se reparte según su capacidad de organización y peso político — en este caso, bancos frente a fintechs.

### 1.4 La fintech: ausencia estructural de regulación de tasas

A diferencia de los dos casos anteriores —donde el BCRA *removió* un límite existente (Com. "A" 8026) o *reservó* un privilegio de acceso (LEFIs)—, el segmento fintech presenta un tercer patrón, más radical: nunca tuvo un tope de tasa que remover. Una guía legal para prestamistas extranjeros (jfcattorneys.com, actualizada jul-2026) confirma que Argentina no impone una tasa de interés máxima legal a los préstamos ordinarios otorgados por Otros Proveedores No Financieros de Crédito (OPNFC, la categoría que incluye a la fintech): el marco regulatorio del BCRA para ese segmento se agota en obligaciones de registración, información y transparencia, no en control de precios. El propio director ejecutivo de la Cámara Argentina Fintech lo planteó como una virtud, no como un vacío, el 24/08/2026: sostuvo textualmente que "Argentina no tiene regulación de tasas" y defendió esa ausencia citando evidencia de que los topes de tasa reducen el acceso al crédito formal antes que la demanda de crédito.

El resultado empírico de esa ausencia de tope es una brecha de costo y de mora muy superior a la del sistema bancario:

- La tasa nominal anual promedio de préstamos personales de proveedores no financieros rondó el 144% en febrero de 2026 (dato BCRA). Casos puntuales relevados por Reuters muestran créditos a trabajadores de plataformas de reparto en torno al 131% TNA y billeteras digitales cercanas al 170% anual.
- La mora del segmento fintech llegó a 31% en junio de 2026, más del doble que el 15% del sistema financiero tradicional en el mismo mes (Monitor de Crédito a las Familias, Facultad de Ciencias Empresariales, Universidad Austral) — y viene subiendo de forma sostenida desde un piso de 3,6% en diciembre de 2024.

El episodio más reciente relevado (03/09/2026) conecta este punto con la sección 2: el BCRA declaró públicamente que bancos y fintech cumplen con las reglas vigentes de información y publicidad de tasas, y que no prevé cambios normativos — comunicado el mismo día en que varios proyectos de ley para poner tope a las tasas se discutían en la Cámara de Diputados. Es un caso que puede leerse simultáneamente en dos registros: como captura en sentido estricto (el statu quo regulatorio, que ya favorece al sector, se ratifica sin cambios pese a la presión legislativa) y como blame avoidance de estrategia de agencia en la tipología de Hood (el BCRA delega la decisión de fondo en el Congreso en lugar de asumirla).

**Una tensión a resolver, no a ocultar:** este hallazgo matiza —no necesariamente contradice— la asimetría bancos/fintech que ya está documentada vía LEFIs. En el terreno del fondeo mayorista (LEFIs), la asimetría favoreció a los bancos. En el terreno de la regulación de tasas al consumidor final, la asimetría corre en sentido inverso: la fintech nunca estuvo sujeta a un tope que los bancos sí tuvieron (aunque parcialmente, y solo para un producto puntual, antes de la Com. "A" 8026). Vale la pena tratar esto como evidencia de que la "asimetría regulatoria" no es un vector único y direccional a favor de un actor, sino que varía según el instrumento regulatorio de que se trate — un matiz que probablemente fortalece el argumento en lugar de debilitarlo, si se explicita en vez de asumir una asimetría pareja en todos los frentes.

## 2. Blame avoidance / framing de responsabilidad (Weaver, 1986)

### 2.1 El argumento de Weaver

R. Kent Weaver, en "The Politics of Blame Avoidance" (*Journal of Public Policy*, 6(4), 371-398, 1986), planteó una inversión respecto del supuesto estándar en ciencia política de que los políticos actúan primariamente para reclamar crédito por políticas exitosas. Weaver argumentó que, en la práctica, evitar el reproche por decisiones impopulares suele pesar más que buscar crédito por decisiones populares. La razón que da es de psicología política: los votantes tienen un sesgo de negatividad — son más sensibles a pérdidas reales o potenciales que a ganancias equivalentes —, lo que hace que el costo político de ser señalado como responsable de un daño supere, en general, el beneficio de ser reconocido por un logro.

De ese argumento se derivan estrategias concretas de evitación de responsabilidad, sistematizadas después por Christopher Hood (2011) en tres categorías: estrategias *presentacionales* (usar el discurso para minimizar o desviar el reproche), estrategias de *política* (elegir la opción que genera menos "flak" o rechazo visible, evitando decisiones que impliquen pérdidas contestables) y estrategias de *agencia* (delegar en otro organismo o actor para diluir la responsabilidad — "encontrar un chivo expiatorio"). Paul Pierson (1994), retomando a Weaver, agrega que estas estrategias también incluyen tácticas ofuscatorias que buscan desacoplar la relación entre una política y sus consecuencias negativas ante el público.

### 2.2 Aplicación al caso: tres episodios, no uno solo

Contra lo que señalaba `planteo_catedra.md` como pendiente, ya hay evidencia de un patrón sostenido durante agosto de 2026, con al menos tres episodios que pueden clasificarse en las categorías de Hood (2011):

1. **Estrategia presentacional — Milei en LN+, 3 de agosto de 2026.** Consultado sobre las familias que no pueden pagar sus créditos, el Presidente respondió preguntando retóricamente si alguien las había obligado a endeudarse, y calificó la refinanciación entre bancos y clientes como "un problema entre privados" (Infobae, 03/08/2026). Es el caso más puro de reencuadre de responsabilidad hacia la decisión individual del deudor.

2. **Estrategia de política — gobierno nacional, 15 de agosto de 2026.** Acá el reencuadre discursivo se usa para justificar una no-decisión: la conducción económica sostuvo que intervenir en la situación de los deudores implicaría trasladar recursos públicos a "una cuestión entre privados" y generaría "riesgo moral" al usar fondos de los contribuyentes para salvar a bancos y deudores (Infobae, 15/08/2026). Este es el caso más relevante de los tres para la teoría: no es solo un enunciado discursivo, sino un argumento técnico (riesgo moral) usado explícitamente para blindar la inacción regulatoria — la variante de "self-limitation of discretion" que Weaver identifica como núcleo del fenómeno.

3. **Continuidad presentacional — nota del BCRA, 27-28 de agosto de 2026.** La nota de "consejos para quienes toman un préstamo" (Infobae, 27/08/2026) no aparece aislada: la cobertura del día siguiente la conecta explícitamente con las declaraciones previas del Presidente y el equipo económico sobre el "problema entre privados" (Infobae, 28/08/2026), mostrando que la nota técnica del BCRA es la traducción institucional de una línea discursiva ya fijada por el Poder Ejecutivo, no una comunicación aislada.

La lectura conjunta de los tres episodios permite hablar de un patrón, no de un caso único: el mismo framing —mora como asunto privado, ajeno al diseño regulatorio— se repite en al menos tres registros distintos (presidencial, técnico-económico y de comunicación institucional del BCRA) en el lapso de un mes, y escala además a disputa política explícita: hacia fines de agosto, la oposición empezó a disputar ese framing atribuyendo la mora al esquema económico oficial en lugar de a decisiones individuales (Cronista, agosto 2026).

### 2.3 El respaldo normativo de fondo: el Régimen de Transparencia

Los tres episodios discursivos de 2026 no aparecen sobre una arquitectura regulatoria neutral: se apoyan en un régimen normativo de larga data que ya encarnaba la misma lógica de responsabilización informativa del deudor, muy anterior al debate coyuntural por la mora récord. El BCRA institucionalizó esa lógica a través de sucesivas comunicaciones:

- **Comunicación "A" 4184** (09/08/2004) — creó el régimen informativo original, dentro de la política "Protección de los Usuarios de Servicios Financieros".
- **Comunicación "A" 6623** (vigente desde 5/1/2019) — detalla qué debe informarse por producto (CFT, TEA, tipo de tasa, condiciones de acceso).
- **Comunicación "A" 7146** (22/10/2020) — extendió el régimen a cooperativas y mutuales como "otros proveedores no financieros de crédito".
- **Comunicación "A" 8203** — texto ordenado vigente (última actualización relevada: 27/02/2025), que consolida el Régimen de Transparencia y fija los "derechos básicos de los usuarios": el cumplimiento normativo pasa por informar claramente (TEA, CFT, leyendas obligatorias visibles), no por limitar sustantivamente lo que la entidad puede cobrar.

El punto teóricamente relevante es que esto le da al blame avoidance discursivo de agosto 2026 un anclaje institucional que lo antecede en dos décadas: la nota de "consejos" no inventa el framing de la decisión informada, lo activa retóricamente sobre una arquitectura regulatoria (el Régimen de Transparencia) que ya definía, desde 2004, que la protección del usuario se resuelve mediante información y comparación, no mediante topes de precio. Esto conecta directamente con la sección 1: mientras que en el caso de la Com. "A" 8026 el BCRA sí removió un límite de precio concreto, el régimen de fondo nunca dependió de esos límites para su lógica de protección — dependía, desde el origen, de la transparencia informativa. Vale la pena explorar en el próximo paso si esta continuidad normativa (transparencia como sustituto de regulación de precios) es un patrón más amplio de diseño regulatorio o específico del segmento de crédito al consumo.

Vale la pena notar la diferencia con la sección 1: mientras la captura regulatoria predice *a favor de quién* se inclina una norma, blame avoidance predice *cómo se comunica* una decisión (o una inacción) para minimizar el costo político de quien la toma — son preguntas distintas, aunque puedan coincidir sobre el mismo episodio.

## 3. Policy feedback (Pierson, 1993)

### 3.1 El argumento de Pierson

Paul Pierson, en "When Effect Becomes Cause: Policy Feedback and Political Change" (*World Politics*, 45(4), 595-628, 1993), plantea que a medida que crece la actividad estatal, las políticas dejan de ser solo *resultados* (efectos) de la política y pasan a ser también *insumos* (causas) que moldean el proceso político futuro — de ahí el título. Pierson identifica dos mecanismos principales por los que una política pasada retroalimenta el comportamiento futuro de los actores:

1. Genera **recursos e incentivos** concretos para actores políticos y económicos (quién gana o pierde acceso a qué, y qué le conviene defender después).
2. Provee **información y señales** que moldean cómo esos actores interpretan el mundo político — expectativas sobre qué es posible o esperable.

La implicancia central para este proyecto es metodológica: policy feedback obliga a mirar la política regulatoria no como un evento aislado (una norma que se sanciona y ya) sino como una secuencia donde cada paso cambia el terreno sobre el que se toma el siguiente.

### 3.2 Aplicación al caso: la secuencia LEFIs y su chequeo empírico

La secuencia que el proyecto ya reconstruyó con datos de `bcra_api.py` es un caso de manual de esta lógica: fin de los pases pasivos/Leliq (2024) → LEFIs como instrumento puente, exclusivo de bancos → fin de LEFIs (10/07/2025, confirmado con la serie 196 del BCRA) → los bancos migran a gestión de liquidez con encajes más altos y mercado secundario (LECAP/BONCAP) → posible traslado a costo de fondeo y de ahí a tasas activas → efecto sobre cuotas y mora.

El hallazgo relevante hasta ahora (sección 2.4 de `planteo_catedra.md`) es que el salto en tasas (BADLAR, préstamos personales) no aparece de inmediato el 10/07/2025 sino con aproximadamente un mes de rezago, en agosto-septiembre 2025 — y que ese salto se desacopla del comportamiento del tipo de cambio en esas mismas ventanas, lo que pesa contra la hipótesis rival de que todo sea ruido pre-electoral. Esto es evidencia compatible con policy feedback (una política pasada — el fin de las LEFIs — generando un efecto rezagado sobre el comportamiento de tasas) pero, como reconoce el propio documento, no cierra el caso: un rezago de repricing bancario de ~1 mes admite varias explicaciones, y hace falta un análisis más fino (spread BADLAR sobre tasa de política monetaria, o un evento-estudio con datos diarios) para consolidarlo como evidencia firme.

## 4. Cómo se articulan los tres mecanismos

Los tres marcos no compiten por explicar el mismo hecho — compiten, cada uno, por ser la mejor explicación de una pieza distinta del diseño regulatorio:

| Mecanismo | Qué explica | Evidencia usada |
|---|---|---|
| Captura regulatoria (Stigler/Peltzman) | *A quién beneficia* una norma puntual (Com. "A" 8026) o un privilegio de acceso (LEFIs) | Series de tasas activas antes/después; exclusividad normativa del instrumento |
| Blame avoidance (Weaver) | *Cómo se comunica* una situación desfavorable para minimizar costo político | Discurso oficial (notas de prensa del BCRA), no normas |
| Policy feedback (Pierson) | *Por qué una política pasada* sigue produciendo efectos sobre el comportamiento de tasas y mora mucho después de sancionada | Series temporales (BADLAR, préstamos personales, tipo de cambio) cruzadas con el timeline regulatorio |

La hipótesis rival que hay que descartar antes de adjudicar cualquiera de estos tres mecanismos (sección 3 de `planteo_catedra.md`) es puramente macroeconómica: que la mora suba por inflación y licuación de ingresos reales, independientemente del diseño regulatorio. Ese descarte se resuelve con el cruce de la sub-pregunta 1 (deuda/ingreso vía EPH) — es el control del diseño, no un cuarto mecanismo en competencia.

## 5. Bibliografía citada en este documento

- Peltzman, S. (1976). Toward a more general theory of regulation. *Journal of Law and Economics*, 19(2), 211-240.
- Pierson, P. (1993). When effect becomes cause: Policy feedback and political change. *World Politics*, 45(4), 595-628.
- Pierson, P. (1994). *Dismantling the welfare state? Reagan, Thatcher, and the politics of retrenchment*. Cambridge University Press.
- Hood, C. (2011). *The blame game: Spin, bureaucracy, and self-preservation in government*. Princeton University Press.
- Stigler, G. J. (1971). The theory of economic regulation. *Bell Journal of Economics and Management Science*, 2(1), 3-21.
- Weaver, R. K. (1986). The politics of blame avoidance. *Journal of Public Policy*, 6(4), 371-398.

### Fuentes periodísticas (episodios de blame avoidance, sección 2.2)

- Infobae (03/08/2026). "¿Alguien les puso una pistola en la cabeza?": qué dijo Milei sobre quienes tomaron créditos y están en mora.
- Infobae (15/08/2026). Mora récord: por qué el Gobierno rechaza asistir a las familias endeudadas.
- Infobae (27/08/2026). En pleno debate por la mora récord, el BCRA publicó consejos para quienes toman un préstamo: cuáles son las recomendaciones.
- Infobae (28/08/2026). Cinco claves a tener en cuenta antes de pedir un crédito para evitar situaciones de morosidad.
- El Cronista (agosto 2026). Javier Milei reunió a su gabinete y se pone al frente de la negociación por las reformas.

### Normativa BCRA citada (sección 2.3, Régimen de Transparencia)

- BCRA. Comunicación "A" 4184 (09/08/2004).
- BCRA. Comunicación "A" 6623 (vigente desde 05/01/2019).
- BCRA. Comunicación "A" 7146 (22/10/2020).
- BCRA. Comunicación "A" 8203 — texto ordenado, "Protección de los Usuarios de Servicios Financieros" (última actualización relevada: 27/02/2025).

### Fuentes citadas (sección 1.4, fintech y ausencia de regulación de tasas)

- JFC Attorneys (jul. 2026). Regulación Fintech en Argentina: Guía Legal 2026.
- Infobae (24/08/2026). El director de la Cámara Fintech defendió al sector: "Poner techo a las tasas reduce el acceso al crédito formal".
- Segundo Enfoque (sept. 2026), citando Reuters. Préstamos por apps en Argentina: la mora llega a récord.
- Ecosistema Startup (ago. 2026), citando Monitor de Crédito a las Familias (Universidad Austral). Fintech Argentina: mora del 31% vs 15% bancario en 2026.
- Ámbito.com (03/09/2026). Tasas de interés: el BCRA considera que bancos y fintech cumplen con las reglas y no prevé cambios en la normativa.

*(Estas referencias son candidatas naturales para consolidar en `docs/bibliografia.md`.)*
