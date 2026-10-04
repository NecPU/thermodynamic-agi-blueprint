# Thermodynamic AGI V4 — Hippocampal Place Cells & Cognitive Tolman Mapping
# Термодинамический AGI V4 — Гиппокампальные клетки места и когнитивное картирование Толланда

**Author & Principal Architect / Автор концепции:** Vakhtang Doundoua / Вахтанг Дундуа (NecPU)  
**Research Phase / Фаза исследования:** V4 Core Specifications (Pre-code Design)  
**Status / Статус:** Living Research Document / Живой развивающийся протокол  

---

## 1. Philosophical & Methodological Shift / Смена парадигмы и методологии

### [EN] Absolute Scientific Realism
In Phase V4, we enforce a strict rule of non-compromise. We completely eliminate the computational "cheat codes" used in previous versions. The agent must solve the environment using ideal, biologically plausible, and non-von Neumann principles. If the Thermodynamic Agent achieves superiority, it must do so strictly through pure Free Energy Principle dynamics without human-engineered mathematical crutches.

### [RU] Абсолютный научный реализм
В Фазе V4 вводится правило жесткого бескомпромиссного моделирования. Мы полностью ликвидируем вычислительные «чит-коды», допущенные на предыдущих этапах. Агент должен решать среду на основе идеальных, биологически правдоподобных и не-фон-неймановских принципов. Если Термодинамический агент побеждает, это должно происходить строго за счет чистой динамики принципа свободной энергии, а не за счет подогнанных человеком эвристик.

---

## 2. Elimination of Unscientific Elements / Ликвидация ненаучных элементов

### [EN] Eradication of the `familiarity` Counter
Phase V3 suffered from a predictive paralysis at a 38% obstacle density due to the integration of a global `familiarity` hash map (step counter per cell). In real physical neuromorphic systems and biological brains, explicit global coordinate hit counters do not exist. This artificial penalty made moving backward over old traces energetically penalizing, trapping the agent in a singularity. **In V4, `familiarity` is completely deleted.**

### [RU] Ликвидация счетчика `familiarity`
Фаза V3 столкнулась с предиктивным параличом при плотности 38% из-за внедрения искусственного параметра `familiarity` (глобального счетчика посещений ячеек). В реальных физических нейроморфных системах и биологическом мозге явных счетчиков посещения координат не существует. Этот штраф делал движение назад по собственным следам энергетически невыгодным, запирая агента в сингулярности. **В V4 параметр `familiarity` полностью уничтожен.**

---

## 3. Mathematical & Neuromorphic Blueprint of V4 / Математический чертеж V4

[EN] To replace artificial heuristics, Phase V4 introduces the Neuromorphic Hippocampal Substrate split into two interconnected layers operating in ideal logic:

[RU] Для замены искусственных эвристик Фаза V4 внедряет нейроморфный гиппокампальный субстрат, разделенный на два взаимосвязанных слоя, работающих в идеальной логике:

### A. Grid Cells / Клетки решетки (Метрический интегратор пути)
* **[EN]** The agent no longer possesses perfect GPS knowledge of the goal. Instead, an internal neural path-integration network tracks displacement vectors based purely on efference copies of motor commands (odometry), introducing realistic accumulation of internal positional entropy into Free Energy Δ F.
* **[RU]** Агент лишается идеального GPS-знания координат цели. Вместо этого внутренняя нейронная сеть интеграции пути отслеживает вектор смещения исключительно на основе эфферентных копий моторных команд (одометрия), внося реалистичное накопление внутренней позиционной энтропии в Свободную Энергию Δ F.

### B. Place Cells & Tolman Graph / Клетки места и когнитивный граф Толланда
* **[EN]** Each unique multimodal feature vector combination \(\mathbf{X}\) triggers the activation of a sparse topological node—a Place Cell (\(P_k\)). Sequential transitions between nodes establish directed synaptic connections (\(M_{ij}\)) via Hebbian plasticity, constructing a predictive Transition Model:
  \[M_{ij} \leftarrow M_{ij} + \eta (P_i \cdot P_j)\]
* **[RU]** Каждая уникальная комбинация мультимодального вектора признаков \(\mathbf{X}\) вызывает активацию разреженного топологического узла — Клетки Места (\(P_k\)). Последовательные переходы между узлами формируют направленные синаптические связи (\(M_{ij}\)) по правилу Хебба, выстраивая предиктивную модель переходов (Transition Model):
  \[M_{ij} \leftarrow M_{ij} + \eta (P_i \cdot P_j)\]

---

## 4. Ideal Resolution of Predictive Paralysis / Разрешение паралича в идеальной логике

### [EN] Invariant Free Energy Paths
When the V4 Thermodynamic Agent enters a dead-end hallway, the Hopfield LTM network registers the obstacle barrier, turning that specific Place Cell node (\(P_{\text{dead}}\)) into a source of high Free Energy. 
When the agent turns around, moving backward along the verified Tolman Graph (\(M_{ji}\)) generates **zero prediction error (ε = 0)** and minimizes variational uncertainty. Going backward becomes the mathematical path of least resistance (absolute confidence), allowing the agent to exit macro-traps naturally without artificial "desperation bonuses".

### [RU] Инвариантные пути свободной энергии
Когда термодинамический агент V4 заходит в тупиковый коридор, сеть Хопфилда фиксирует барьер, превращая конкретный узел клетки места (\(P_{\text{dead}}\)) в источник высокой свободной энергии. 
При развороте агента движение назад по проверенному когнитивному графу (\(M_{ji}\)) генерирует **нулевую ошибку предсказания (ε = 0)** и полностью минимизирует вариационную неопределенность. Возврат назад становится математически траекторией наименьшего сопротивления (абсолютной уверенности), позволяя агенту естественно покидать макро-ловушки без искусственных «бонусов отчаяния».

---

## 5. Evolution Tracking Metrics / Метрики эволюции бенчмарка

| Metric Reference / Параметр | Phase V3 Status / Состояние V3 | Phase V4 Target / Цель Фазы V4 |
| :--- | :--- | :--- |
| **Exploration Engine / Движок поиска** | Local Steps / Локальные ячейки | Macro Cognitive Graph / Макро-граф |
| **Hallway Recovery / Возврат из ловушек** | Blocked by `familiarity` (Stuck) | Path of Zero Prediction Error ε |
| **Goal Positioning / Вектор цели** | Omniscient Static Vector | Seeded Grid Cell Odometry |
| **Scientific Integrity / Чистота логики** | Partial (Heuristic Crutch present) | **Absolute (100% Pure Active Inference)** |

---
*This document will be updated dynamically as the mathematical modules of the Hippocampal Place Network are formalized locally.*

© 2026 Vakhtang Doundoua (NecPU). All rights reserved. / Все права защищены.
