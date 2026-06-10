# 경력기술서 요약

## Senior Embedded Audio / DSP SDK Integration Engineer

임베디드·자동차 오디오 환경에서 DSP SDK를 실제 제품 타겟에 통합하고, 메모리·MIPS 제약 분석과 튜닝·검증·릴리즈까지 수행한 16년차 엔지니어입니다.

핵심 메시지:
- Automotive, TWS & AI Edge, Android, Embedded Linux 환경에서 오디오/DSP SDK 플랫폼 포팅 및 통합 수행
- Telechips TCC8050 Subcore (차량용 헤드유닛) 및 ADI SHARC+ 차량용 외장 앰프 기반 Automotive 오디오 SDK 통합 및 최적화
- 이기종 TWS DSP 칩셋(QCC, Airoha, BES, Bluetrum, Goodix) 및 GAP9 (AI Edge) SDK 포팅 및 Fixed-point/SIMD 최적화
- Android App/Framework/HAL/DSP 전 레이어에 걸친 SDK 이식 및 오디오 지연 분석
- Python 기반 튜닝 UI/제어 도구 구축으로 현장 파라미터 조정 및 고객 대응 절차 표준화

## 대표 프로젝트

### 1. Automotive 오디오 SDK 포팅 및 통합 (헤드유닛 & 외장 앰프)

회사/기간: 가우디오랩, 2024.01 - 현재
기여도: 50~100%

- 문제/요구사항: 차량용 헤드유닛 및 외장 앰프 환경의 리소스/플랫폼 제약 극복
- 역할: Telechips TCC8050 Subcore(RTOS/Bare-metal) 환경 오디오 SDK 포팅 및 동작 제어
- 역할: NVIDIA Tegra X2 타겟 AI Inference SDK 포팅 및 GStreamer 미디어 재생 경로 통합
- 역할: ADI SHARC+(ADSP-21569/21835) 및 Audio Weaver 기반 SDK 통합 및 연산/메모리 최적화
- 결과: 하드웨어 제약(MIPS, Memory)을 극복하고 실차 구동 안정성 확보 및 Python 기반 실차 튜닝 도구 구축

### 2. TWS & AI Edge SDK 통합 및 최적화

회사/기간: 가우디오랩, 2021.09 - 2023.12
기여도: 50~100% (프로젝트별 상이)

- 문제: 이기종 DSP 및 AI Edge 프로세서의 하드웨어 리소스 제약 극복
- 역할: QCC514x/515x/517x, Airoha AB1565/1577/1585, BES2600YP, Bluetrum BT8951, Goodix PoC 등 칩셋별 통합 포인트 정의 및 IMU 헤드 트래킹, 지연/버퍼 분석
- 역할: GAP9(저전력 AI) 타겟 AI Inference SDK 포팅 및 입출력 버퍼 연동 안정화
- 역할: SIMD/Fixed-point 최적화로 제한된 DSP 연산/메모리 환경에서 실행 안정성 개선
- 결과: 이기종 DSP 및 AI Edge 타겟 통합 버전 릴리즈 및 튜닝/검증 대응 체계 확보

### 3. Android Audio SDK 통합 및 지연 분석

회사/기간: 가우디오랩, 2021.03 - 2021.09
기여도: 80%

- 문제: Android 오디오 경로의 레이어별 지연과 제약이 달라 SDK 적용 위치에 따른 리스크가 큼
- 역할: App/Framework/HAL/DSP 레이어별 지연 유발 구간과 통합 제약을 분해해 비교
- 역할: DSP 우선 통합, HAL 대체 통합, Audio Effect 제한 적용 기준 문서화
- 결과: Oboe/ExoPlayer 기반 앱 검증으로 재생 경로별 동작 차이를 확인하고 통합 의사결정 기준 확보

## 보조 제품화 경험

- Linux/Android 월패드와 IoT 플랫폼(REST/MQTT/SIP) 연동 제품화 및 RS-485 병목 완화
- Tizen Studio Installer/Package Manager 및 VS Code Extension 기반 개발도구 운영성 개선
- Android 앱, 웹 모니터링, 셋탑박스 APP/Middleware 개발을 통한 상용 임베디드 제품 개발·릴리즈 경험 확보

## 기술 요약

- 핵심 통합: Embedded Audio SDK, DSP SDK, SDK Integration, Automotive Audio SDK, TWS DSP, Android Audio
- 최적화: DSP Library, Fixed-point, SIMD, Memory/MIPS Optimization, Latency/Buffer Analysis
- 플랫폼: Embedded Linux, Android, RTOS / Bare-metal, ADI SHARC+, Qualcomm Hexagon DSP, QCC, Airoha, NVIDIA Tegra X2, GAP9
- 미디어/프레임워크: Audio Weaver, SigmaStudio, WebRTC, GStreamer, Android Audio HAL/Effect
- 품질/릴리즈: 정적 분석, 동적 분석, 단위/통합 테스트 자동화, Jenkins 기반 빌드/배포
