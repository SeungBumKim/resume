# 경력기술서 요약

## Senior Embedded Audio / DSP SDK Integration Engineer

임베디드·자동차 오디오 환경에서 DSP SDK를 실제 제품 타겟에 통합하고, 메모리·MIPS 제약 분석과 튜닝·검증·릴리즈까지 수행한 16년차 엔지니어입니다.

핵심 메시지:
- Automotive, TWS, Android, Embedded Linux 환경에서 오디오/DSP SDK 제품화 수행
- ADI SHARC+ 기반 Automotive Amp SDK 통합 및 제약 환경 최적화
- ADI SHARC+ 기반 Automotive Amp SDK 통합 과정에서 Program/Data Memory 및 MIPS 제약 완화
- Python 기반 튜닝 UI/제어 도구 구축으로 현장 파라미터 조정 및 고객 대응 절차 표준화
- SDK 적용 위치, 버퍼/지연, 메모리/MIPS 제약, 검증·릴리즈 기준을 구조화하는 데 강점

## 대표 프로젝트

### 1. Automotive Amp SDK 개발/통합 및 튜닝 툴 구축

회사/기간: 가우디오랩, 2025.01 - 현재
기여도: 80%

- 문제: 차량 DSP 타겟의 Program/Data Memory와 MIPS 제약으로 초기 포팅 상태의 제품 적용성이 제한됨
- 역할: Automotive Amp SDK의 입출력, 제어, 파라미터, 상태 경로를 정리하고 ADI SHARC+/Audio Weaver 기반 플랫폼 통합 수행
- 역할: DSP Library 기반 연산 경로 최적화, 메모리 배치/사용량 조정, 불필요 연산 제거로 제약 구간 해소
- 결과: 초기 포팅 상태에서 제품 적용을 어렵게 하던 Program/Data Memory 및 MIPS 제약 완화
- 결과: Python 기반 튜닝 UI/제어 도구를 개발해 현장 파라미터 조정과 고객 대응 절차 표준화

### 2. TWS DSP SDK 통합

회사/기간: 가우디오랩, 2021.09 - 2023.12
기여도: 60~100% (프로젝트별 상이)

- 문제: QCC/Airoha 등 칩셋별 오디오 체인, 센서, 제어 경로가 달라 동일 SDK의 제품 적용 방식이 매번 달라짐
- 역할: 칩셋별 SDK 통합 포인트를 정의하고 IMU 헤드 트래킹, 지연/버퍼, 제어 경로 분석 수행
- 역할: SIMD/Fixed-point 최적화로 제한된 DSP 연산/메모리 환경에서 실행 안정성 개선
- 결과: Airoha 타겟 통합 버전 릴리즈 및 고객 타겟별 튜닝/검증 대응 체계 확보

### 3. Android Audio SDK 통합 및 지연 분석

회사/기간: 가우디오랩, 2021.03 - 2021.09
기여도: 80%

- 문제: Android 오디오 경로의 레이어별 지연과 제약이 달라 SDK 적용 위치에 따른 리스크가 큼
- 역할: App/Framework/HAL/DSP 레이어별 지연 유발 구간과 통합 제약을 분해해 비교
- 역할: DSP 우선 통합, HAL 대체 통합, Audio Effect 제한 적용 기준 문서화
- 결과: Oboe/ExoPlayer 기반 앱 검증으로 재생 경로별 동작 차이를 확인하고 통합 의사결정 기준 확보

### 4. AI Inference SDK 미디어 경로 통합 및 다중 플랫폼 확장

회사/기간: 가우디오랩, 2024.01 - 2024.12
기여도: 50%

- 문제: 타겟별 빌드/런타임 차이와 미디어 입출력 경로 차이로 SDK 적용 범위가 제한됨
- 역할: CPU/GPU/Edge(GAP9, Tegra) 타겟의 공통 포팅 레이어와 검증 절차 정리
- 역할: WebRTC/GStreamer 경로에 SDK를 삽입하고 입출력 버퍼 처리 안정화
- 결과: 실서비스 미디어 경로에서 AI Inference SDK를 검증할 수 있는 다중 플랫폼 베이스라인 구축

## 보조 제품화 경험

- Linux/Android 월패드와 IoT 플랫폼(REST/MQTT/SIP) 연동 제품화 및 RS-485 병목 완화
- Tizen Studio Installer/Package Manager 및 VS Code Extension 기반 개발도구 운영성 개선
- Android 앱, 웹 모니터링, 셋탑박스 APP/Middleware 개발을 통한 상용 임베디드 제품 개발·릴리즈 경험 확보

## 기술 요약

- 핵심 통합: Embedded Audio SDK, DSP SDK, SDK Integration, Automotive Amp SDK, TWS DSP, Android Audio
- 최적화: DSP Library, Fixed-point, SIMD, Memory/MIPS Optimization, Latency/Buffer Analysis
- 플랫폼: Embedded Linux, Android, ADI SHARC+, Qualcomm Hexagon DSP, QCC, Airoha, Tegra, GAP9
- 미디어/프레임워크: Audio Weaver, SigmaStudio, WebRTC, GStreamer, Android Audio HAL/Effect
- 품질/릴리즈: 정적 분석, 동적 분석, 단위/통합 테스트 자동화, Jenkins 기반 빌드/배포
