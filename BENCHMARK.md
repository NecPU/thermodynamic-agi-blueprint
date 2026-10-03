================================================================================
TECHNICAL SPECIFICATION & INTERFACE LEGEND: THERMODYNAMIC AGI V2 BENCHMARK
Core Build: 2026-03-21 | Interactive Verification Protocol & Substrate Analysis
================================================================================

--------------------------------------------------------------------------------
LEGAL DISCLAIMER & COPYRIGHT NOTICE
--------------------------------------------------------------------------------
* Original Architecture & Blueprint Framework: (C) 2026 Vakhtang Doundoua (NecPU)
* Author Profile: Vakhtang Doundoua
* Author GitHub Profile: https://github.com
* Contact & R&D Communications: doundoua.v@gmail.com
* Licensing Node: Distributed strictly under the "Custom Sovereign AGI Blueprint License".
  Any utilization, academic replication, or deployment of the VETO inhibitor or 
  dead-end compression graph models must preserve direct attribution to the author.

================================================================================
ENGLISH VERSION (TECHNICAL SPECIFICATIONS)
================================================================================

1. SIMULATION ARCHITECTURE & CORE ENHANCEMENTS

This interface provides a real-time validation environment comparing a standard, 
history-dependent Contextual Autoregressive AI (Transformer/LLM reasoning abstraction) 
against the Thermodynamic AGI V2 paradigm (rooted in Active Inference and Free 
Energy Minimization).

The simulation runs in a discrete 16x16 spatial grid topology with an adjustable 
obstacle density slider. Both systems operate under identical environmental perception 
rules, interacting exclusively through the unified Environment.perceiveDirection() API.

Symmetrical Resource Allocation:
* Actuator Cost: Executing a mechanical step requires a fixed fee (actuatorCost = 10), 
  deducted STRICTLY UPON SUCCESSFUL SPATIAL ALTERATION (coordinate modification). 
  If a movement fails (striking a wall) or is preempted, the physical energy remains untouched.
* Thinking Cost: The core baseline differentiator, processed per discrete time step (Tock).

Compared Computational Paradigms:

* Contextual Autoregressive AI (Linear History Window):
  Simulates token-by-token text generation processing. Every positional frame and 
  adjacent vector is appended into an uncompressed history log.
  - Context Bloat: Memory grows linearly over time: N_tokens proportional to Tocks.
  - Inference Explosion: Compute overhead scales directly with context sequence length: 
    Cost_compute = N_tokens * 0.05. This simulates standard attention matrix multiplication 
    complexity. In complex spaces, the mere computational overhead of maintaining 
    historical text logs causes premature energy collapse (DEPLETED).

* Thermodynamic AGI V2 (Active Inference & Bounded Mapping):
  Operates via a predictive virtualization loop. Prior to physical motor activation, 
  the internal state machine virtualizes 4 sensory-motor vectors, consuming a fixed 
  computing fee (4 * Psi_sim).
  - Perfect Structural Compression: States are organized into an invariant graph of 
    structural features (World Model). Memory footprint is tightly bounded by the 
    environment's total cell volume (N_cells <= SIZE^2) and remains invariant to rollout time.
  - Dead-End Invariant Mapping: If the agent enters an enclosed space where 3 out of 4 
    directions are impassable (composed of physical walls or previously marked dead-ends), 
    it dynamically extracts a Dead-End Invariant. Using its historical position tracker 
    (prevRow/prevCol) to understand the backtrack path, the agent permanently flags this 
    coordinate in its internal deadEnds register, mapping it out of the solution space.
  - Predictive VETO Inhibitor: When evaluating prospective steps, any cell marked within 
    the deadEnds register returns an absolute Variational Free Energy limit (Delta F = +Infinity). 
    The top-down VETO inhibitor intercepts the motor execution line. The agent completely 
    preserves its kinetic energy reserve (Actuator_cost = 0), suppresses redundant steps, 
    and redirects its trajectory toward unmapped regions.

2. CONTROL PANEL & INTERFACE LEGEND

* STARTING ENERGY: The initial metabolic reservoir allocated to both agents (Range: 50 - 3000). 
  It establishes the operational rollout bounds before absolute energy exhaustion.
* PSI_SIM (Simulation Cost): Scaling parameter adjusting the internal processing tax 
  for predictive virtualization. Total flat-rate compute fee per Tock is set to 4 * Psi_sim.
* ACTUATOR COST: The physical force tax for executing a step. Symmetrical for both models; 
  completely preserved when a VETO activates.
* GAMMA (Curiosity Weight): Scales the mathematical drive toward unknown topography. 
  Amplifies Free Energy (Delta F) reduction incentives when exploring states with zero 
  or low familiarity.
* OBSTACLE RATIO (Map Density): Dynamically scales maze generation density between 15% and 45%. 
  Increasing density creates deep networks of tight corridors and dead-end traps, 
  accelerating the Autoregressive Context Explosion.
* RANDOM SEED: Numerical seed feeding the pseudoRandom generator to ensure reproducible 
  map geometries. An automated BFS validation script checks for absolute pathway solvability; 
  impossible maps are structurally rejected at compilation time.
* Energy Dynamics Chart: Real-time display mapping out energy consumption per Tock. 
  The Red Line (Autoregressive) exhibits an exponential/parabolic decay curve due to scaling 
  attention overhead. The Green Line (Thermodynamic) displays a highly optimized, linear 
  trajectory with clear plateaus visualizing active VETO preservation cycles.


================================================================================
РУССКАЯ ВЕРСИЯ (ТЕХНИЧЕСКИЕ СПЕЦИФИКАЦИИ)
================================================================================

1. АРХИТЕКТУРА СИМУЛЯЦИИ И КЛЮЧЕВЫЕ МЕХАНИЗМЫ

Данный интерфейс представляет собой среду верификации в реальном времени, сравнивающую 
классический, зависимый от истории Контекстный авторегрессионный ИИ (абстракция рассуждений 
Трансформеров/LLM) и парадигму Thermodynamic AGI V2, построенную на принципах 
Активного инференса и минимизации свободной энергии.

Симуляция выполняется в дискретной топологии сетки 16x16 с динамически регулируемым 
ползунком плотности препятствий. Оба агента взаимодействуют со средой на 100% симметрично 
через унифицированный интерфейс Environment.perceiveDirection().

Симметричная физика затрат ресурсов:
* Стоимость действия: Физический шаг требует фиксированного расхода энергии (actuatorCost = 10), 
  который списывается СТРОГО ПРИ УСПЕШНОМ ИЗМЕНЕНИИ КООРДИНАТ. Если движение заблокировано 
  стеной или отменено внутренним цензором, кинетическая энергия полностью сохраняется.
* Стоимость мышления: Главный дифференциатор вычислительной сложности, списываемый 
  на каждом такте времени (Tock).

Сравниваемые парадигмы мышления:

* Contextual Autoregressive AI (Линейное окно истории):
  Имитирует покомпонентную генерацию текста. Модель вынуждена непрерывно записывать координаты 
  и сенсорные данные соседей в контекст в виде бесконечной ленты токенов.
  - Раздувание памяти: Объем контекста линейно растет во времени: N_tokens пропорционально Tocks.
  - Взрыв инференса: Стоимость вычислений на каждом тике увеличивается пропорционально накопленной истории: 
    Cost_compute = N_tokens * 0.05, симулируя сложность матричного перемножения механизмов внимания (Attention). 
    На сложных дистанциях налог на обработку прошлых логов приводит к тепловой смерти и истощению энергии (DEPLETED).

* Thermodynamic AGI V2 (Активный инференс и структурное сжатие):
  Работает через контур предиктивной виртуализации. Перед каждым шагом внутренняя модель 
  обсчитывает 4 ортогональных направления исходов, расходуя фиксированную вычислительную цену (4 * Psi_sim).
  - Идеальное сжатие: Значения упаковываются в инвариантный граф признаков реальности (World Model). 
    Размер памяти жестко ограничен геометрией лабиринта (N_cells <= SIZE^2) и не зависит от времени блуждания.
  - Топологическое картирование тупиков (Dead-End Invariant Mapping): Если агент заходит в замкнутую 
    зону, где 3 из 4 направлений заблокированы (физическими стенами или уже выжженными тупиками), 
    система динамически извлекает тупиковый инвариант. Опираясь на внутренний трекер прошлой позиции 
    (prevRow/prevCol) для определения пути назад, агент перманентно маркирует эту координату 
    в реестре deadEnds, полностью исключая её из пространства решений.
  - Предиктивный механизм ВЕТО: При оценке шагов ячейка из реестра тупиков возвращает 
    абсолютный предел Вариационной Свободной Энергии (Delta F = +Infinity). Сквозной оператор — 
    ингибитор ВЕТО — мгновенно блокирует команду на актуаторы. Система полностью сберегает 
    физическую энергию движения (Actuator_cost = 0), окрашивает тупик на карте в тёмно-красный цвет 
    и перенаправляет вектор поиска в неисследованные зоны лабиринта.

2. ЛЕГЕНДА ЭЛЕМЕНТОВ УПРАВЛЕНИЯ ДАШБОРДА

* STARTING ENERGY: Стартовый пул метаболической энергии агентов (Диапазон: 50 - 3000). 
  Устанавливает предел жизнеспособности до наступления энергетического голодания.
* PSI_SIM (Simulation Cost): Коэффициент вычислительных затрат на предиктивную виртуализацию 
  одного направления. Итоговый расход на мышление за один такт зафиксирован на уровне 4 * Psi_sim.
* ACTUATOR COST: Физическая стоимость движения тела робота. Одинакова для обеих моделей; 
  полностью сохраняется при срабатывании ВЕТО.
* GAMMA (Curiosity Weight): Вес когнитивного любопытства. Математически увеличивает выигрыш 
  в снижении свободной энергии (Delta F) при обнаружении клеток с низким уровнем знакомства.
* OBSTACLE RATIO (Map Density): Регулятор плотности лабиринта (от 15% до 45%). 
