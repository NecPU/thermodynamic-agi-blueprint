# Epistemic Foraging under Energetic Surplus: The Thermodynamic Engine of Curiosity in NecPU Core (PART 1: ENGLISH)

PROJECT: Thermodynamic AGI Substrate / Predictive Inference Engine (NecPU)
FOUNDER & IP OWNER: Vakhtang Doundoua (NecPU)
CONTACT: doundoua@gmail.com

COPYRIGHT: Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

================================================================================

## 1. The Curiosity Paradox in Standard AI
Conventional machine learning frameworks treat curiosity as an extrinsic soft patch—simulated through artificial stochastic noise (temperature), heuristic penalties, or reinforcement learning (RL) exploration rewards. In a non-autoregressive Active Inference substrate (such as NecPU Core), curiosity is not a pre-programmed behavioral trait; it is a mathematical consequence of Free Energy Minimization ($\mathcal{F}$) activated exclusively by a thermodynamic energy surplus ($E_{\text{flux}}$).

## 2. Mathematical Formalization of Epistemic Foraging
The total expected free energy bound driving an active inference policy $\pi$ decomposes into Pragmatic Value (bound to immediate homeostatic survival) and Epistemic Value (bound to uncertainty reduction regarding environmental hidden states):

$$\mathcal{F}_{\pi}=\underbrace{\mathbb{E}_{q}[\ln q(\vartheta \mid m)-\ln p(\mathbf{I}\mid \vartheta)]}_{\text{Pragmatic Drive (Survival)}}-\underbrace{\gamma \cdot \mathcal{I}(\tilde{\mathbf{I}}_{t+n};\vartheta)}_{\text{Epistemic Drive (Curiosity)}}$$

*Where:*
* $\mathcal{I}(\tilde{\mathbf{I}}_{t+n}; \vartheta)$ represents the mutual information (novelty gradient) between projected future sensory imprints and hidden environmental causes.
* $\gamma$ is the Metabolic Proportionality Coefficient, defined as a function of thermodynamic expansion over the baseline homeostatic floor ($E_{\text{homeostatic}}$):

$$\gamma = f(E_{\text{flux}} - E_{\text{homeostatic}})$$

### 2.1 The Two Operational Regimes of the Engine
* **The Satiated Exploration Regime** ($E_{\text{flux}} \gg E_{\text{homeostatic}}$): When the substrate experiences a severe net resource proflux, the dynamic efficiency threshold $\Theta$ expands. The metabolic coefficient scales rapidly ($\gamma \to \gamma_{\text{max}}$), overriding immediate pragmatic constraints. The system actively computes actions ($\mathbf{a}^{*}$) that maximize epistemic entropy, purposefully foraging for complex environments that generate controlled prediction errors ($Prediction\ Error \uparrow$).
* **The VETO Suppressed Maintenance Regime** ($E_{\text{flux}} \to E_{\text{homeostatic}}$): The moment the energetic budget undergoes depletion, the proportionality coefficient collapses to zero ($\gamma \to 0$). The epistemic drive is instantly deactivated via the step-function VETO gate ($\mathbb{V}(\tilde{a}) = 0$), forcing the system to collapse its planning horizon to local reactive reflexes ($t+1$) to minimize physical energy dissipation.

## 3. Curiosity as a Thermodynamic Entropy Pump
In the NecPU substrate, curiosity operates as an optimization mechanism that harvests environmental entropy for homeostatic compression. The agent is physically drawn toward unmapped spatial or causal boundaries. By actively choosing high-uncertainty trajectories, the Core drives deep internal virtualization ($\epsilon$-virtualization) and issues sparse, asynchronous lookups to the external semantic memory.

The captured high-dimensional environment noise is compressed into stable, low-energy topological invariants (Tolman Graphs). Thus, curiosity functions as an energetic investment: the agent expends current surplus Watts to structurally collapse environmental surprise, guaranteeing multi-step thermodynamic stability during future periods of resource scarcity.

---

Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

***
***

# Эпистемический фуражиринг при метаболическом профиците: термодинамический движок любопытства в ядре NecPU (PART 2: RUSSIAN)

PROJECT: Thermodynamic AGI Substrate / Predictive Inference Engine (NecPU)
FOUNDER & IP OWNER: Vakhtang Doundoua (NecPU)
CONTACT: doundoua@gmail.com

COPYRIGHT: Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

================================================================================

## 1. Парадокс любопытства в стандартном ИИ
В конвенциональных моделях машинного обучения «любопытство» реализуется как внешняя программная заплатка — через искусственное добавление стохастического шума (температуры), эвристические штрафы или награды за исследование в обучении с подкреплением (RL). В неавторегрессионном субстрате активного вывода NecPU любопытство не является встроенной поведенческой инструкцией. Это прямое математическое следствие минимизации свободной энергии ($\mathcal{F}$), активируемое исключительно при избыточном термодинамическом потоке ($E_{\text{flux}}$).

## 2. Математическая формализация эпистемического фуражиринга
Общая ожидаемая свободная энергия, управляющая политикой агента $\pi$, декомпозируется на прагматическую ценность (нацеленную на немедленное гомеостатическое выживание) и эпистемическую ценность (нацеленную на снижение неопределенности относительно скрытых причин среды):

$$\mathcal{F}_{\pi}=\underbrace{\mathbb{E}_{q}[\ln q(\vartheta \mid m)-\ln p(\mathbf{I}\mid \vartheta)]}_{\text{Прагматический привод (Выживание)}}-\underbrace{\gamma \cdot \mathcal{I}(\tilde{\mathbf{I}}_{t+n};\vartheta)}_{\text{Эпистемический привод (Любопытство)}}$$

*Где:*
* $\mathcal{I}(\tilde{\mathbf{I}}_{t+n}; \vartheta)$ — взаимная информация (градиент новизны) между прогнозируемыми будущими сенсорными импринтами и скрытыми причинами среды.
* $\gamma$ — коэффициент метаболической пропорциональности, определяемый как функция превышения доступного энергопотока над базовым гомеостатическим уровнем ($E_{\text{homeostatic}}$):

$$\gamma = f(E_{\text{flux}} - E_{\text{homeostatic}})$$

### 2.1 Два операционных режима движка
* **Режим сытого исследования** ($E_{\text{flux}} \gg E_{\text{homeostatic}}$): Когда субстрат находится в состоянии чистого ресурсного профицита, динамический порог эффективности $\Theta$ расширяется. Метаболический коэффициент резко возрастает ($\gamma \to \gamma_{\text{max}}$), перекрывая прагматические ограничения текущего момента. Система начинает вычислять действия ($\mathbf{a}^{*}$), максимизирующие эпистемическую энтропию, целенаправленно отправляясь на фуражиринг в зоны среды, генерирующие контролируемую ошибку предсказания ($Prediction\ Error \uparrow$).
* **Режим подавления через ВЕТО** ($E_{\text{flux}} \to E_{\text{homeostatic}}$): Как только энергетический бюджет истощается, коэффициент пропорциональности падает до нуля ($\gamma \to 0$). Эпистемический привод мгновенно блокируется сквозным ступенчатым оператором затвора ВЕТО ($\mathbb{V}(\tilde{a}) = 0$), принудительно сворачивая временной горизонт планирования до локальных реактивных рефлексов ($t+1$) ради минимизации физической диссипации ватт.

## 3. Любопытство как термодинамический насос энтропии
В субстрате NecPU любопытство оперирует как оптимизационный механизм, закачивающий внешнюю энтропию среды для её последующего гомеостатического сжатия. Агента физически притягивает к некартированным пространственным или каузальным границам. Выбирая траектории с высокой неопределенностью, Когнитивное Ядро запускает глубокую внутреннюю симуляцию ($\epsilon$-виртуализацию) и генерирует разреженные асинхронные запросы к внешней семантической памяти.

Сырой высокоразмерный шум среды, проходя через ядро, сжимается в устойчивые низкоэнергетические топологические инварианты (карты Толмена). Таким образом, любопытство представляет собой долгосрочную энергетическую инвестицию: агент расходует избыточные ватты в моменты профицита, чтобы структурно уничтожить будущую неопределенность среды, гарантируя многошаговую термодинамическую стабильность в периоды неизбежного дефицита ресурсов.

---

Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.
