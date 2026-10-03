# Interactive Thermodynamic Benchmark: Active Inference vs. Autoregressive Context Explosion

Original Repository: https://github.com/NecPU/thermodynamic-agi-blueprint
Author/Developer: Vakhtang Doundoua (GitHub: https://github.com/NecPU), doundoua@gmail.com
License & Copyright: Custom Sovereign AGI Blueprint License. All Rights Reserved.

================================================================================
ENGLISH VERSION
================================================================================

1. Simulation Description

This interactive simulator visually demonstrates the physical and computational dead-end of context-dependent autoregressive architectures (Transformer/LLM models) during long-horizon planning tasks, while validating the efficiency of the Thermodynamic AGI V2 paradigm rooted in Active Inference and Free Energy Minimization.

Architecture & Mathematical Framework:
Both agents are deployed into an identical discrete environment (a 16 x 16 grid-world maze) with procedurally generated obstacles and guaranteed path solvability. Their objective is to navigate to the goal state while managing a strict budget of starting energy (2000 units). The underlying physics of computation and movement are strictly symmetrical:

1. Unified Perception API: Agents interact with the grid exclusively via the Environment.perceiveDirection() interface, parsing neighboring spatial data. Any asymmetric data access or "hidden global map cheating" is structurally eliminated.
2. Symmetrical Energy Dynamics (Compute vs. Actuator):
   * Actuator Cost: Physical execution of motor commands demands a rigid, fixed fee (actuatorCost) and is only deducted upon successful coordinate alteration in the physical space.
   * Compute / Inference Cost: The primary operational differentiator, capturing the intrinsic computational complexity expended per discrete time step (Tock).

Compared Paradigms:

* Contextual Autoregressive AI (Linear History):
  Emulates a traditional Autoregressive Transformer. On every cycle, the agent is forced to append its current coordinates and spatial observations into a continuous context window as a sequence of raw data tokens.
  - Memory Bloat: The context size (Linear Context Memory) scales linearly over time: N_tokens proportional to Tocks.
  - Inference Explosion: The computational overhead per tick scales directly with historical sequence length: Cost_compute = N_tokens * 0.05, accurately mirroring standard Attention Complexity scaling. Over long rollouts, the mere tax of processing past context becomes astronomically expensive, inducing thermodynamic death and premature energy starvation (DEPLETED).

* Thermodynamic AGI V2 (Active Inference):
  Constructs a dense, compressed cognitive graph of environmental invariants (World Model). Prior to physical execution, the agent models 4 sensory-motor vectors within its internal virtualization engine.
  - Perfect Structural Compression: Memory scale is fundamentally bounded by the geometric constraints of the maze grid (N_cells <= 256) and remains completely invariant to time duration.
  - Fixed Inference Overhead: Computational processing cost remains completely static across all steps: Cost_compute = 4 * PSI_SIM.
  - The VETO Mechanism: If the internal predictive simulation reveals that all prospective paths yield high Free Energy (Delta F) updates—such as hitting dead-ends or highly redundant states—the internal VETO inhibitor triggers. The agent overrides the physical actuators, paying a flat computation fee for "thought" while preserving the physical move energy entirely.

2. Interface and Controls Legend

Control Panel (Left Sidebar):
* STARTING ENERGY: The initial energy matrix allocated to both agents at session launch (range: 50 - 3000). It establishes the operational lifespan of the system, determining how deep a rollout the model can sustain before hitting absolute energy starvation (DEPLETED).
* PSI_SIM (Simulation Cost): The exact computational cost required to predictively model a single spatial vector within the internal virtualization engine of the Thermodynamic AGI. Because the agent pre-scans 4 directions every turn, the flat baseline fee for "thinking" is structurally locked at 4 * PSI_SIM per step.
* ACTUATOR COST: The physical energy consumed by the robot's physical hardware to execute a single kinetic movement within the maze. It is deducted strictly symmetrically for both agents, and only upon successful coordinate modification. When the internal VETO overrides an action, this energy is completely preserved.
* GAMMA (Curiosity Weight): A critical thermodynamic driver that scales the agent’s mathematical drive toward unmapped topology. It amplifies Free Energy (Delta F) reduction incentives when encountering states with zero or minimal familiarity values, preventing cyclic dead-ends and optimizing discovery.
* RANDOM SEED: A unique numerical identifier feeding the pseudoRandom generator. It guarantees identical structural layouts for the 16 x 16 grid. If a seed maps out an impossible layout, the simulator's built-in BFS auto-increments the seed until a verified solvable path is generated.

Action Buttons:
* Generate Map: Triggers procedural generation of a new maze geometry based on a random or user-defined seed and resets both agents back to the origin state (0,0).
* Run Simulation / Stop Simulation: Toggles a continuous automated execution loop for both architectures at a fixed interval of 175ms, running until success, depletion, or reaching the hard execution limit of 800 ticks.
* Step (1 Tock): Manually processes a single discrete computational and kinetic step for both models simultaneously, enabling fine-grained, frame-by-frame structural inspection.

Chart: Energy Dynamics per Tock:
* X-Axis (Tocks): Discrete simulation time steps.
* Y-Axis (Energy): The remaining real-time energy reserve of the respective model.
* Red Line (Contextual AR): Illustrates the accelerated, non-linear collapse of the energy baseline caused by the compounding tax of historical context processing. Visually defines the AR scaling wall.
* Green Line (Thermodynamic V2): Highlights a highly stable, linear decay curve. The intermittent plateaus and changes in slope visually capture the dynamic activation of the VETO inhibitor, preserving actuator energy.

Benchmark Verdict: Under identical physical environmental constraints, the Autoregressive AI inevitably suffers a catastrophic thermal collapse due to contextual memory accumulation, whereas the Thermodynamic model securely reaches the goal state maintaining strict efficiency and predictable operational overhead.


================================================================================
РУССКАЯ ВЕРСИЯ (RUSSIAN VERSION)
================================================================================

1. Описание симуляции

Этот интерактивный симулятор наглядно демонстрирует физический и вычислительный тупик контекстно-зависимых авторегрессионных архитектур (Transformer/LLM) в задачах долгосрочного планирования и выявляет фундаментальные преимущества парадигмы Thermodynamic AGI V2, построенной на принципах Активного инференса (Active Inference) и минимизации свободной энергии.

Архитектура и математическая модель:
Оба агента помещаются в идентичную дискретную среду (лабиринт 16 x 16) со случайной процедурной генерацией препятствий и верифицируемой проходимостью. Их цель — достичь целевой точки, расходуя ограниченный пул стартовой энергии (2000 единиц). Физика вычислений и перемещений строго симметрична:

1. Единое окно восприятия (Unified Perception API): Агенты взаимодействуют со средой исключительно через метод Environment.perceiveDirection(), считывая состояние соседних клеток. Скрытое преимущество в «зрении» или доступе к глобальной карте полностью исключено.
2. Симметричная физика затрат (Compute vs Actuator):
   * Стоимость действия (Actuator Cost): Физическое перемещение тела робота стоит фиксированную цену (actuatorCost) и списывается только при успешном изменении координат на поле.
   * Стоимость мышления (Compute / Inference Cost): Это ключевой дифференциатор сложности вычислений, списываемый на каждом такте времени (Tock).

Сравниваемые парадигмы:

* Contextual Autoregressive AI (Линейная история):
  Модель имитирует работу стандартного Трансформера. На каждом шаге она вынуждена записывать свои координаты и сенсорные данные соседей в контекстное окно в виде бесконечной ленты токенов.
  - Раздувание памяти: Размер памяти (Linear Context Memory) линейно растет во времени: N_tokens пропорционально Tocks.
  - Взрыв инференса: Стоимость вычислений на каждом тике растет линейно от размера накопленной истории: Cost_compute = N_tokens * 0.05. Это идеально симулирует вычислительную сложность механизмов внимания (Attention Complexity). На длинных дистанциях стоимость простого «размышления» становится астрономической, приводя к тепловой смерти и истощению энергии агента (DEPLETED).

* Thermodynamic AGI V2 (Активный инференс):
  Агент строит компактную вероятностную карту мира (World Model) в виде графа инвариантов. Перед каждым шагом он запускает мысленное моделирование четырех направлений во внутреннем виртуальном контуре.
  - Идеальное сжатие (Perfect Compression): Память агента ограничена исключительно геометрическим размером лабиринта (N_cells <= 256) и полностью независима от времени блуждания.
  - Фиксированный инференс: Стоимость мышления строго стабильна на каждом тике: Cost_compute = 4 * PSI_SIM.
  - Механизм ВЕТО: Если внутренняя симуляция показывает, что все доступные шаги ведут в тупик или пройденные зоны (резкий рост свободной энергии Delta F), активируется ингибиторное ВЕТО. Агент блокирует работу актуаторов, платя фиксированную цену за «мысль», но полностью сберегая физическую энергию движения (actuatorCost).

2. Легенда интерфейса и элементов управления

Панель управления (Сайдбар слева):
* STARTING ENERGY (Стартовая энергия): Начальный запас энергии, выделяемый обоим агентам при старте сессии (диапазон: 50 - 3000). Определяет «запас прочности» системы. Показывает, насколько далеко модель может продвинуться, прежде чем наступит энергетическое истощение (DEPLETED).
* PSI_SIM (Simulation Cost / Стоимость мысленной симуляции): Коэффициент вычислительных затрат на обсчет одного направления во внутреннем виртуальном контуре Thermodynamic ИИ. На каждом шаге агент предиктивно сканирует 4 направления, поэтому фиксированный расход энергии за «мыслительный» такт всегда равен 4 * PSI_SIM.
* ACTUATOR COST (Стоимость действия): Физическая энергия, затрачиваемая телом робота на выполнение одного шага в лабиринте. Списывается строго одинаково для обоих агентов и только в случае успешного физического перемещения (изменения координат). При срабатывании механизма ВЕТО у термодинамического агента эта энергия полностью сберегается.
* GAMMA (Curiosity Weight / Вес любопытства): Параметр термодинамического агента, определяющий его внутреннее стремление к исследованию неизвестных зон. Математически увеличивает выигрыш в снижении свободной энергии (Delta F) при обнаружении клеток с нулевым или низким уровнем знакомства (familiarity), заставляя агента эффективнее искать выходы и избегать циклов.
* RANDOM SEED (Случайное зерно генерации): Числовой идентификатор для генератора псевдослучайных чисел (pseudoRandom). Гарантирует воспроизводимость геометрии лабиринта 16 x 16. Если сгенерированный лабиринт не имеет решения, BFS-алгоритм симулятора автоматически скорректирует сид в большую сторону до тех пор, пока не построит гарантированно проходимый маршрут.

Кнопки действий:
* Generate Map (Сгенерировать карту): Создает новую конфигурацию стен лабиринта на основе случайного или заданного сида и сбрасывает состояние агентов на стартовую позицию (0,0).
* Run Simulation / Stop Simulation (Запуск / Остановка): Включает непрерывный автоматический цикл шагов («тактов») для обеих моделей с интервалом в 175 мс до тех пор, пока они не дойдут до цели, не истощат энергию или не исчерпают лимит времени (800 тиков).
* Step (1 Tock) (Один шаг): Принудительно выполняет строго один такт вычислений и движения для обоих агентов одновременно, позволяя детально изучить пошаговый расход ресурсов.

График: Energy Dynamics per Tock (Динамика энергии):
* Ось X (Tocks): Дискретные такты времени симуляции.
* Ось Y (Energy): Текущий баланс энергии агентов.
* Красная линия (Contextual AR): Показывает параболическое или ускоренное падение энергии из-за постоянного роста стоимости инференса внимания. Наглядно демонстрирует системный тупик авторегрессии.
* Зеленая линия (Thermodynamic V2): Демонстрирует линейный и стабильный расход ресурсов. Изломы и плато на графике визуализируют работу механизмов ВЕТО, где физическая энергия сохраняется.

Вывод бенчмарка: При равной сложности физических условий авторегрессионный ИИ неизбежно погибает от вычислительного перегрева из-за раздувания памяти контекста, в то время как Thermodynamic ИИ достигает цели с минимальными и строго контролируемыми затратами энергии.
