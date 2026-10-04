# Thermodynamic AGI V3 — Academic Verification & Attractor Benchmark Protocol
# Термодинамический AGI V3 — Протокол академической верификации и аттракторных метрик

**Author & Principal Architect / Автор концепции:** Vakhtang Doundoua / Вахтанг Дундуа (NecPU)  
**Verification Build / Версия сборки:** 2026-10-04 · Strict Scientific Parity Mode  

---

## 1. Experimental Setup & Constraints / Параметры экспериментальной среды
[EN] The V3 benchmark evaluates spatial optimization and compute-tax boundaries under the strict percolation threshold of a 16×16 maze geometry.
[RU] Бенчмарк V3 оценивает пространственную оптимизацию и границы вычислительного налога в условиях жесткого порога перколяции на геометрии лабиринта 16×16.

* **Obstacle Ratio (Плотность препятствий):** 38% (Critical percolation limit / Критический предел)
* **Actuator Cost (Стоимость актуатора):** 20.00 energy units per physical step
* **Starting Budget (Стартовый бюджет):** 2000.0 energy units
* **Compute Tax (Базовый налог восприятия):** 4 * PSI_SIM (Fixed 4.0 energy per tock)

---

## 2. Computational Cost Equations / Математика вычислительных затрат

### Autoregressive Baseline (Transformer Span) / Авторегрессионный ИИ:
\[Cost_{\text{AR}} = (0.05 \cdot |historyLog|) + (4 \cdot \Psi_{\text{sim}}) + ActuatorCost\]
* *Result:* Linear complexity scaling. The KV-cache equivalent causes explosive energy consumption as the agent explores the grid.
* *Итог:* Линейное масштабирование сложности. Аналог KV-кэша вызывает лавинообразное потребление энергии по мере исследования сети.

### Thermodynamic Paradigm (Active Inference + LTM) / Термодинамический ИИ (NecPU):
\[Cost_{\text{Thermo}} = 4 \cdot \Psi_{\text{sim}} + (ActuatorCost \cdot \Theta_{\text{VETO}})\]
* *Result:* Invariant O(1) compute complexity. Inference costs are fixed locally within the 4×3 synaptic matrix W and 4×4 Hopfield network T.
* *Итог:* Инвариантная сложность вычислений O(1). Затраты на инференс жестко фиксированы локально внутри синаптической матрицы W 4x3 и сети Хопфилда T 4x4.

---

## 3. Empirical Stress-Test Data / Результаты эмпирических стресс-тестов

| Paradigm / Парадигма ИИ | Physical Steps / Шаги | Max Tock Cost / Макс. такт | VETO Triggers / Торможения | Final Status / Итог | Residual Energy / Остаток |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Autoregressive (Красный)** | 77 | **7.85** | 0 | **DEPLETED** (Выгорание) | -2.1 |
| **Thermodynamic (Зеленый)** | 17 | **4.00** | **174** | **ACTIVE** (Выживание) | **784.0** |

### Core Discovery / Главное научное открытие Фазы V3:
[EN] Under extreme obstacle density (38%), the Autoregressive agent enters context collapse, burning its entire energy budget on memory cache overhead. The Thermodynamic agent successfully compresses spatial boundaries, executes 174 autoassociative VETOs via Hopfield energy minimization, blocks physical degradation, and preserves the physical substrate's hardware.
[RU] В условиях экстремальной плотности (38%) Авторегрессионный агент впадает в контекстный коллапс, сжигая весь бюджет на удержание кэша памяти. Термодинамический агент успешно сжимает пространственные границы, совершает 174 автоассоциативных ВЕТО через минимизацию энергии Хопфилда, блокирует физическое разрушение и полностью сохраняет аппаратную платформу.

---
© 2026 Vakhtang Doundoua (NecPU). All rights reserved. / Все права защищены.
