# NecPU Proof-of-Concept (PoC) Benchmarks & Algorithmic Simulators

**Author:** Vakhtang Doundoua (NecPU)  
**Contact:** doundoua@gmail.com  
**Repository:** https://github.com/NecPU/thermodynamic-agi-blueprint  
**DOI:** https://10.5281/zenodo.23262980

---

## PART 1: ENGLISH DOCUMENTATION

### 1. Purpose and Epistemic Scope (Honest PoC Boundaries)
This directory contains zero-dependency Python algorithmic simulators demonstrating the core thermodynamic optimization mechanisms specified in [`../LLM_THERMODYNAMIC_VETO.md`](../LLM_THERMODYNAMIC_VETO.md).

To maintain strict scientific rigor, please note the scope of these benchmarks:
* **Algorithmic Verification:** All thresholds (Θ), layer-pass reductions, vector averages, cosine similarities, and FP16 memory footprints are computed dynamically at runtime—no benchmark metrics are hardcoded.
* **Simulation Input:** Both scripts operate on deterministic synthetic token streams (`TokenStep` and `KVTokenEntry`) rather than full-scale neural network weights on a GPU cluster. Actual production savings on live models (e.g., 70B+ parameter Transformers) scale dynamically with the informational density of the prompt and available metabolic budget ($E_{\text{total}}$).
* **Zero External Dependencies:** Built strictly on the Python 3.8+ standard library (`dataclasses`, `typing`, `math`) for instant reproducibility in any terminal or GitHub Codespace.

---

### 2. Included Benchmarks

#### A. Thermodynamic VETO Gating (`llm_veto_poc.py`)
Demonstrates the discrete step-function inhibitory operator $\mathbb{V}(\tilde{a})$ and metabolic threshold contraction $\Theta = f(1 / E_{\text{total}})$ across an 80-layer Transformer stack (REFLEX_CORE_LAYERS = 12):
1. **Early-Exit VETO Bypass:** Halts upper-layer execution on low-novelty tokens ($\Delta I \approx 0$).
2. **Hallucination VETO Abort:** Blocks token generation when Variational Free Energy spikes above the dynamic threshold ($F \ge \Theta$).
3. **Metabolic CoT Throttling:** Contracts $\Theta$ from 1.96(95% energy surplus) down to0.65 (12% critical deficit), collapsing deep Chain-of-Thought ([CoT]) horizons into a 12-layer survival reflex mode.

**Verified Terminal Output:**
```text
AGGREGATED THERMODYNAMIC BENCHMARK SUMMARY:
  * Standard Transformer Compute : 960 layer-passes (100.0% energy baseline)
  * NecPU VETO Gated Compute     : 280 layer-passes (29.2% energy used)
  * Net Compute & Energy Saved   : 70.8% (Landauer-bound gating active)
```

---

#### B. Strutinsky Dual-Scale KV-Cache Compression (`strutinsky_kv_cache_poc.py`)
Demonstrates the Strutinsky Shell Correction Isomorphism (Section 2.3 of `LLM_THERMODYNAMIC_VETO.md`) across a 16-token context window ($d_{\text{head}} = 128$, FP16):
1. **Microscopic Shell Correction (Invariant Retention):** Preserves high-novelty causal anchors and mathematical axioms (`E_crit=0.10`, `Theta=f(1/E)`, `t+1`) in exact FP16 slots with **100.0% fidelity**.
2. **Macroscopic Smoothing (Liquid-Drop Compression):** Averages low-novelty syntactic filler ($\Delta I < 0.25$) into compressed macro-vectors (`MACRO_BLOCK_SIZE = 4`), mitigating the von Neumann memory-bus bottleneck.


**Verified Terminal Output:**
```text
AGGREGATED STRUTINSKY KV-CACHE BENCHMARK SUMMARY:
  * Standard Linear KV-Cache     : 16 slots (8,192 bytes | 100.0% VRAM baseline)
  * Strutinsky Dual-Scale Cache  :  7 slots (3,584 bytes | 43.8% VRAM used)
  * Structural Invariant Fidelity: 100.0% (Zero quantization loss on critical axioms)
  * Memory & Bus Bandwidth Saved : 56.2% (Von Neumann bottleneck mitigated)
```

---

### 3. Quick Start

Run either benchmark directly from the repository root:

```bash
python3 examples/llm_veto_poc.py
python3 examples/strutinsky_kv_cache_poc.py
```

---

### 4. License & Attribution

This work is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org) (CC BY-NC 4.0); see [`../LICENSE`](../LICENSE).

Commercial use (including commercial deployment, hardware manufacturing, or integration into proprietary systems) requires a separate written agreement with the author: doundoua@gmail.com.

Requested attribution: "Original Non-Autoregressive AGI Architecture by Vakhtang Doundoua (NecPU)", with a link to this repository.

Author: Vakhtang Doundoua (also spelled Dundua; Вахтанг Дундуа), NecPU.

Cite all versions: https://10.5281/zenodo.23262980

---
Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.

---
---

# Бенчмарки доказательства концепции (PoC) и алгоритмические симуляторы NecPU

**Автор:** Вахтанг Дундуа (NecPU)  
**Контакты:** doundoua@gmail.com  
**Репозиторий:** https://github.com/NecPU/thermodynamic-agi-blueprint  
**DOI:** https://10.5281/zenodo.23262980

---

## ЧАСТЬ 2: РУССКАЯ ДОКУМЕНТАЦИЯ

### 1. Назначение и границы применимости (честный статус PoC)
В этой директории размещены автономные алгоритмические симуляторы на языке Python без внешних зависимостей, демонстрирующие базовые механизмы термодинамической оптимизации из спецификации [`../LLM_THERMODYNAMIC_VETO.md`](../LLM_THERMODYNAMIC_VETO.md).

Для сохранения строгой научной прозрачности важно учитывать границы данных тестов:
* **Честная алгоритмическая проверка:** Все динамические пороги (Θ), сокращения проходов по слоям, усреднения векторов, косинусные сходства и объемы памяти FP16 вычисляются в реальном времени при запуске скриптов — заранее заданных («захардкоженных») результатов в коде нет.
* **Синтетический входной поток:** Оба скрипта работают на детерминированных тестовых последовательностях токенов (`TokenStep` и `KVTokenEntry`), а не на весах многомиллиардной нейросети на GPU-кластере. В реальных системах (например, на трансформерах класса 70B+) итоговая экономия зависит от информационной плотности конкретного запроса и текущего запаса энергии ($E_{\text{total}}$).
* **Отсутствие сторонних библиотек:** Код использует только стандартную библиотеку Python 3.8+ (`dataclasses`, `typing`, `math`) и мгновенно запускается в любом терминале или среде GitHub Codespaces.

---

### 2. Состав бенчмарков

#### А. Термодинамическое шлюзование VETO (`llm_veto_poc.py`)
Демонстрирует работу дискретного ступенчатого оператора торможения $\mathbb{V}(\tilde{a})$ и сжатие метаболического порога $\Theta = f(1 / E_{\text{total}})$ на стеке из 80 слоев трансформера (REFLEX_CORE_LAYERS = 12):
1. **Ранний выход (Early-Exit VETO Bypass):** Отключает вычисления верхних слоев на информационно пустых токенах ($\Delta I \approx 0$).
2. **Блокировка галлюцинаций (Hallucination VETO Abort):** Прерывает генерацию токена при скачке вариационной свободной энергии выше допустимого порога ($F \ge \Theta$).
3. **Метаболическое дросселирование CoT:** При падении заряда с 95% до 12% порог $\Theta$ сжимается с 1.96до0.65, сворачивая глубокие цепочки рассуждений ([CoT]) в 12-слойный рефлекторный режим выживания.

**Подтвержденный вывод терминала:**
```text
AGGREGATED THERMODYNAMIC BENCHMARK SUMMARY:
  * Standard Transformer Compute : 960 layer-passes (100.0% energy baseline)
  * NecPU VETO Gated Compute     : 280 layer-passes (29.2% energy used)
  * Net Compute & Energy Saved   : 70.8% (Landauer-bound gating active)
```

---

#### Б. Двухмасштабное сжатие KV-кэша по Струтинскому (`strutinsky_kv_cache_poc.py`)
Демонстрирует изоморфизм оболочечной поправки В. М. Струтинского (раздел 2.3 спецификации `LLM_THERMODYNAMIC_VETO.md`) на контекстном окне из 16 токенов ($d_{\text{head}} = 128$, точность FP16):
1. **Микроскопическая оболочечная поправка (сохранение инвариантов):** Критически важные причинные якоря и математические аксиомы (`E_crit=0.10`, `Theta=f(1/E)`, `t+1`) сохраняются в отдельных ячейках FP16 со **100.0% точностью** без потерь квантования.
2. **Макроскопическое сглаживание (жидкокапельное сжатие):** Фоновые синтаксические связки с низким приростом информации ($\Delta I < 0.25$) объединяются в усредненные макро-векторы (`MACRO_BLOCK_SIZE = 4`), снижая нагрузку на шину памяти Фон Неймана.

**Подтвержденный вывод терминала:**
```text
AGGREGATED STRUTINSKY KV-CACHE BENCHMARK SUMMARY:
  * Standard Linear KV-Cache     : 16 slots (8,192 bytes | 100.0% VRAM baseline)
  * Strutinsky Dual-Scale Cache  :  7 slots (3,584 bytes | 43.8% VRAM used)
  * Structural Invariant Fidelity: 100.0% (Zero quantization loss on critical axioms)
  * Memory & Bus Bandwidth Saved : 56.2% (Von Neumann bottleneck mitigated)
```

---

### 3. Быстрый запуск

Запустите любой из бенчмарков из корневой директории репозитория:

```bash
python3 examples/llm_veto_poc.py
python3 examples/strutinsky_kv_cache_poc.py
```

---

### 4. Лицензия и указание авторства

Работа распространяется по лицензии [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org) (CC BY-NC 4.0); см. [`../LICENSE`](../LICENSE).

Коммерческое использование (включая коммерческое внедрение, производство оборудования и интеграцию в проприетарные системы) требует отдельного письменного соглашения с автором: doundoua@gmail.com.

Просьба указывать авторство: "Original Non-Autoregressive AGI Architecture by Vakhtang Doundoua (NecPU)" со ссылкой на этот репозиторий.

Автор: Вахтанг Дундуа (Vakhtang Doundoua, также Dundua), NecPU.

Цитировать все версии: https://10.5281/zenodo.23262980

---
Copyright © 2026 Vakhtang Doundoua (NecPU). Licensed under CC BY-NC 4.0 — see LICENSE.
