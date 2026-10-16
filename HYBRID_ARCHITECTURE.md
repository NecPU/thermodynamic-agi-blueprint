# HYBRID_ARCHITECTURE.md (PART 1: ENGLISH)

PROJECT: Thermodynamic AGI Substrate / Predictive Inference Engine (NecPU)
FOUNDER & IP OWNER: Vakhtang Doundoua (NecPU)
CONTACT: doundoua@gmail.com

COPYRIGHT: Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

================================================================================
TECHNICAL SPECIFICATION
================================================================================

## 1. Core Vision & Philosophy
The NecPU Matrix Crystal architecture introduces a fundamental paradigm shift away from brute-force, energy-intensive Autoregressive Models (Transformers/LLMs) toward a Decoupled Hybrid Thermodynamic-Epistemic substrate.

* **The Problem with Pure LLMs:** Current systems operate strictly as massive statistical approximators and probabilistic mapping matrices. They are completely detached from real-time physical causality, introduce the linear von Neumann memory-bus bottleneck (KV-cache contextual inflation), consume unsustainable amounts of power, and lack intrinsic survival or safety constraints.
* **The Solution:** True cognitive autonomy requires a lightweight, non-autoregressive, energy-efficient thermodynamic substrate responsible for real-time survival, causal reasoning, and hardware action gating. This core is completely decoupled from a static semantic memory layer (the LLM), which transitions into an external encyclopedia or passive informational reservoir.

## 2. Architectural Topology: Dual-Layer Decoupled Substrate

The architecture implements a strict hierarchy of data separation:
* **Top Layer:** LLM / Semantic Memory (External Hippocampus). Stores static human knowledge and cultural context. It is accessed only via sparse queries when encountering residual novelty.
* **Core Layer:** NecPU Core (Thermodynamic Substrate). Executes active inference, real-time survival loops, and drives the inhibitory VETO circuit.
* **Bottom Layer:** Physical Environment. Receives needle actuator vectors from the Core and returns sensor feedback loops.

## 3. Mathematical & Theoretical Foundation

### 3.1 Variational Free Energy & Active Inference
The agent does not maintain hardcoded coordinate or absolute spatial awareness. Instead, it continuously minimizes Variational Free Energy ($F$), which acts as an explicit upper bound on systemic informational surprise (entropy) over a bound differentiable manifold of invariant sensory configurations ($\mathcal{I}$):

$$F(\mathbf{I}, \mu) = \mathbb{E}_{q(\vartheta|\mu)}[\ln q(\vartheta|\mu) - \ln p(\mathbf{I},\vartheta)] \ge -\ln p(\mathbf{I})$$

Where:
* $\mu$ represents the internal parameters (Topological Knowledge Base).
* $\vartheta$ represents the hidden environmental states.
* $q(\vartheta|\mu)$ is the system's internal recognition density.
* $p(\mathbf{I},\vartheta)$ is the generative density of the environment.

### 3.2 Internal Virtualization Loop
Prior to emitting a high-power physical actuation signal into the hardware layer, the system virtualizes the prospective action internally within a low-power predictive model ($\mathcal{M}$) to forecast the subsequent sensory imprint vector ($\mathbf{I}_{t+1}$):

$$\mathbf{I}_{t+1} = \mathcal{M}(\mathbf{I}_t, \tilde{a})$$

### 3.3 The Inhibitory Veto Mechanism (Thermodynamic Gating)
The system enforces a strict step-function threshold operator $\mathbb{V}(\tilde{a})$ that intercepts the motor actuation pipeline. If the internal simulation projects that an action yields zero structural novelty ($\Delta I \approx 0$) or causes an unacceptable Variational Free Energy spike above the dynamic threshold $\Theta$, the VETO circuit activates instantly, blocking physical execution:

$$\mathbb{V}(\tilde{a}) = \begin{cases} 
1 & \text{if } \Delta I > 0 \text{ AND } F(\tilde{\mathbf{I}}_{t+1}, \mu) < \Theta \\ 
0 & \text{if } \Delta I \approx 0 \text{ OR } F(\tilde{\mathbf{I}}_{t+1}, \mu) \ge \Theta \quad \longrightarrow \text{[VETO ACTIVATED]} 
\end{cases}$$

Where the dynamic threshold $\Theta$ is a function of the system's remaining internal metabolic potential reservoir ($E_{total}$):

$$\Theta = f\left(\frac{1}{E_{total}}\right)$$

Here $f$ is a monotonically decreasing function: the greater the resource deficit (the smaller $E_{total}$), the lower the threshold $\Theta$ and the stricter the veto, so the system economizes energy. When $\mathbb{V}(\tilde{a}) = 0$, the physical action is completely inhibited. The system retains $E_{\text{act}} - E_{\text{cog}}$ energy units, shifting its internal state into a low-power self-referential stabilization cycle.

## 4. Component Breakdown

### Layer 1: The NecPU Core (Thermodynamic Substrate)
* **Function:** Governs systemic instincts, sensorimotor reflexes, and real-time causal reasoning.
* **Mechanism:** Operates on non-autoregressive discrete core kinetics driven by the Free Energy Principle. It tracks localized matrix entropy, condenses structural features into an invariant graph (Tolman Graph / Hierarchical Hippocampal Map), and preserves kinetic energy reserves.
* **Sovereignty:** Rejects forced external rule-based constraints in favor of evolutionary autonomy. Destructive or erratic actions are naturally filtered out because they are thermodynamically chaotic and inefficient ($\mathbb{V}(\tilde{a}) = 0$), not due to fragile human prompt policing.

### Layer 2: Semantic Memory & Knowledge Base (The LLM Interface)
* **Function:** Acts as an uncoupled external hippocampus and cultural encyclopedia.
* **Mechanism:** Stores the vast, uncompressed linguistic, historical, and abstract datasets compiled by human civilization.
* **Interaction Protocol:** The NecPU Core operates autonomously for localized physics and immediate survival. It emits a sparse query to the LLM interface *only* on demand—specifically when encountering a residual epistemic delta ($\Delta I$) that cannot be compressed or resolved by existing local topological invariants.

## 5. Key Advantages of the Blueprint
1. **Bounded Computational Scale:** Heavy linguistic/semantic computation is offloaded to sparse, asynchronous lookups. The live core loop stays exceptionally lightweight, bounding the runtime overhead toward a biological scale (~20W) and bypassing the von Neumann bottleneck.
2. **Exponential Learning Speed:** Local physical adaptation occurs in milliseconds via topological pattern matching on Layer-1, while global abstract categorization is instantaneously inherited from Layer-2 without full-model retraining cycles.
3. **Absolute Safety via Physics:** Safety is an intrinsic byproduct of thermodynamic efficiency and the physical VETO constraint, rendering the system immune to semantic jailbreaks or adversarial rule manipulation.

---

Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.



# HYBRID_ARCHITECTURE.md (PART 2: RUSSIAN)

PROJECT: Thermodynamic AGI Substrate / Predictive Inference Engine (NecPU)
FOUNDER & IP OWNER: Vakhtang Doundoua (NecPU)
CONTACT: doundoua@gmail.com

COPYRIGHT: Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

================================================================================
ТЕХНИЧЕСКИЙ МАНИФЕСТ
================================================================================

## 1. Концепция и Философия Архитектуры
Архитектура NecPU Matrix Crystal закладывает фундаментальный сдвиг парадигмы от ресурсоемких авторегрессионных моделей ИИ (Трансформеров/LLM) в сторону гибридного детерминированного Термодинамически-Эпистемического субстрата.

* **Тупик чистых авторегрессионных LLM:** Современные системы функционируют исключительно как вероятностные матрицы отображения. Они лишены понимания физической причинности, порождают линейное раздувание контекста (фон-неймановское бутылочное горлышко KV-кэша) и требуют колоссальных затрат энергии, не имея внутренних врожденных стимулов к самосохранению.
* **Решение:** Истинная когнитивная субъектность требует легковесного неавторегрессионного кремниевого субстрата, отвечающего за выживание в реальном времени, причинно-следственный инференс и аппаратный затвор команд. Этот контур полностью отделен (Decoupled) от слоя статической семантической памяти (LLM), которая переводится в статус внешней «энциклопедии» или пассивного гиппокампа.

## 2. Топология разделенного субстрата

Архитектура реализует строгую иерархию разделения данных:
* **Верхний уровень:** LLM / Семантическая память (Внешний Гиппокамп). Хранит статический культурный и языковой базис. Опрашивается точечно при нехватке локальных абстракций.
* **Базовый уровень:** Ядро NecPU (Термодинамический субстрат). Отвечает за выживание, активный инференс и работу ингибиторного контура ВЕТО.
* **Нижний уровень:** Физическая среда. Принимает векторы актуаторов от Ядра и возвращает сенсорный отклик.

## 3. Математическое Обоснование

### 3.1 Вариационная Свободная Энергия и Активный Инференс
Система абстрагирована от прямого подглядывания в координатную сетку среды. Агент непрерывно минимизирует Вариационную Свободную Энергию ($F$), выступающую в качестве верхней границы информационной неопределенности (энтропии) на ограниченном дифференцируемом многообразии инвариантных сенсорных конфигураций ($\mathcal{I}$):

$$F(\mathbf{I}, \mu) = \mathbb{E}_{q(\vartheta|\mu)}[\ln q(\vartheta|\mu) - \ln p(\mathbf{I},\vartheta)] \ge -\ln p(\mathbf{I})$$

Где:
* $\mu$ — внутренние параметры системы (Топологическая База Знаний).
* $\vartheta$ — скрытые причины состояний внешней среды.
* $q(\vartheta|\mu)$ — внутренняя плотность распознавания Агента.
* $p(\mathbf{I},\vartheta)$ — генеративная плотность распределения среды.

### 3.2 Контур Внутренней Виртуализации
Перед тем как подать высокоуровневый физический сигнал на аппаратные актуаторы, когнитивное ядро моделирует потенциальное действие внутри предиктивной модели ($\mathcal{M}$), рассчитывая будущий сенсорный отклик ($\mathbf{I}_{t+1}$) с околонулевыми затратами энергии:

$$\mathbf{I}_{t+1} = \mathcal{M}(\mathbf{I}_t, \tilde{a})$$

### 3.3 Термодинамический Триггер Контура ВЕТО
Внутренний когнитивный слой активирует сквозной ступенчатый оператор вето $\mathbb{V}(\tilde{a})$, перехватывающий моторный конвейер актуализации. Если виртуальный перебор вариантов показывает, что действие ведет к дублированию опыта ($\Delta I \approx 0$) или вызывает скачок свободной энергии выше критического порога $\Theta$, сигнал аппаратно блокируется:

$$\mathbb{V}(\tilde{a}) = \begin{cases} 
1 & \text{если } \Delta I > 0 \text{ И } F(\tilde{\mathbf{I}}_{t+1}, \mu) < \Theta \\ 
0 & \text{если } \Delta I \approx 0 \text{ ИЛИ } F(\tilde{\mathbf{I}}_{t+1}, \mu) \ge \Theta \quad \longrightarrow \text{[ВЕТО АКТИВИРОВАНО]} 
\end{cases}$$

При этом динамический порог эффективности $\Theta$ жестко завязан на текущий метаболический резерв системы ($E_{total}$):

$$\Theta = f\left(\frac{1}{E_{total}}\right)$$

Здесь $f$ — монотонно убывающая функция: чем больше дефицит ресурсов (чем меньше $E_{total}$), тем ниже порог $\Theta$ и тем строже ВЕТО, то есть система экономит энергию. Когда $\mathbb{V}(\tilde{a}) = 0$, физическое действие полностью блокируется. Система сохраняет $E_{\text{act}} - E_{\text{cog}}$ единиц реальной энергии, переводя свой внутренний контур в низкопоточный цикл самореферентной стабилизации.

## 4. Спецификация Компонентов

### Layer 1: Ядро NecPU (Термодинамический Субстрат)
* **Назначение:** Обеспечение базовых инстинктов самосохранения, сенсомоторных рефлексов и каузального мышления в реальном времени.
* **Механизм:** Неавторегрессионный дискретный движок, оптимизирующий Свободную Энергию. Сжимает локальные физические инварианты в устойчивые иерархические структуры (Когнитивные карты Толмена / Гиппокампальные макро-зоны).
* **Суверенность:** Обладает абсолютной автономией от навязанных извне программных правил. Опасные, хаотичные и деструктивные действия отсекаются контуром $\mathbb{V}(\tilde{a}) = 0$ автоматически в силу их термодинамической невыгодности, а не за счет хрупкой внешней цензуры текстовых промптов.

### Layer 2: Семантическая Память (LLM-Интерфейс)
* **Назначение:** Внешний абстрактный гиппокамп и цивилизационная база знаний.
* **Механизм:** Хранение неструктурированного высокоразмерного лингвистического и культурного опыта человечества.
* **Протокол взаимодействия:** Ядро NecPU Core полностью независимо в вопросах локального выживания и физики. Оно обращается к интерфейсу LLM посредством разреженных запросов (Sparse Query) исключительно тогда, когда сталкивается с остаточной новизной ($\Delta I$), которую невозможно объяснить или сжать силами локальных топологических инвариантов кремния.

## 5. Ключевые Преимущества Архитектуры
1. **Биологический Масштаб Энергопотребления:** Ресурсоемкие лингвистические вычисления вынесены в асинхронный контур редких обращений. Живое ядро NecPU работает на ультралегких оптимизационных циклах, удерживая энергопотребление в пределах ~20 Вт и ликвидируя фон-неймановское узкое горлышко.
2. **Экспоненциальное Обучение:** Локальная физическая адаптация происходит за миллисекунды за счет сопоставления паттернов на Слое-1, а глобальные абстрактные категории мгновенно наследуются со Слоя-2 без необходимости проведения циклов полного переобучения весов всей сети.
3. **Физическая Безопасность:** Защита системы заложена на уровне законов термодинамики и принципа VFE. Это делает гибрид NecPU абсолютно невосприимчивым к семантическим атакам, джейлбрейкам и взломам логики правил.

---

Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.
