# 경력기술서 요약

## Senior Embedded / Platform Software Engineer

상용 임베디드 제품과 플랫폼 소프트웨어를 개발해온 17년차 엔지니어입니다. 최근에는 다양한 OS·SoC 환경에서 SDK 개발, 시스템 통합, 성능 분석, 검증·릴리즈를 수행했습니다.

핵심 메시지:
- 상용 Embedded APP/Middleware 개발, Linux/Android 제품 플랫폼 제품화, SDK 개발·통합으로 이어진 제품 소프트웨어 경력
- Android·TWS DSP·AAOS/Embedded Linux·AI Edge 환경에서 공통 SDK 개발·통합 및 성능·자원 제약 분석
- 테스트 자동화와 CI/CD 기반 검증·릴리즈 절차 운영

## 대표 프로젝트

### 1. Cross-platform SDK 개발 및 제품화

회사/기간: 가우디오랩, 2021.03 - 현재
기여도: 50~100%

- 배경/과제: OS·하드웨어·자원 제약이 다른 제품 환경에서 공통 SDK의 적용성 확보
- 책임 범위: 타깃 요구사항과 자원 제약을 분석해 SDK를 구현·개발하고 Public API를 설계하며, 플랫폼별 통합·검증 방식을 정의
- 핵심 구현: Android·TWS DSP·AAOS IVI/Embedded Linux·AI Edge의 오디오 경로와 입출력 제약을 분석해 SDK 통합·안정화 수행
- 결과: 성능·호환성 이슈 분석과 CI/CD 기반 검증·릴리즈 절차를 통해 타깃별 적용 기준과 릴리즈 재현성 확보

#### 1-1. 차량용 내장 앰프 헤드유닛 SDK 개발·포팅

회사/기간: 가우디오랩, 2026년 - 현재

- 배경/과제: Qualcomm SA 계열 양산 대상 및 Telechips AAOS 기반의 각 내장 앰프 헤드유닛 환경에서 오디오 SDK의 제품 적용성 확보
- 책임 범위: 타깃별 SDK 기능 개발·포팅, 오디오 경로 통합, 동작 안정화와 검증 수행
- 핵심 구현: 각 헤드유닛의 오디오 경로와 플랫폼 제약을 분석해 SDK 적용 방식 구현
- 튜닝 도구: 전용 제어·파라미터 튜닝 도구를 개발해 헤드유닛 타깃 검증과 튜닝에 활용
- 양산 적용: Qualcomm SA 헤드유닛의 양산 적용을 위한 SDK 개발·포팅과 검증 수행
- 결과: Memory/MIPS·지연·버퍼 이슈를 분석하고 타깃별 검증·릴리즈 절차 수행

#### 1-2. 차량용 외장 앰프 SDK 통합 및 최적화

회사/기간: 가우디오랩, 2025년

- 배경/과제: 외장 앰프 DSP 환경의 연산·메모리 제약 속에서 공통 오디오 SDK의 제품 적용성 확보
- 책임 범위: ADI SHARC+ DSP·Audio Weaver 환경의 SDK 기능 개발·통합 방식과 검증 기준을 정리하고 제품 동작 안정화 수행
- 핵심 구현: Memory/MIPS·지연·버퍼 이슈를 분석하고 자원 제약에 맞춘 최적화 적용
- 튜닝 도구: 전용 제어·파라미터 튜닝 도구를 개발해 외장 앰프 타깃의 검증과 튜닝에 활용
- 결과: 외장 앰프 타깃의 SDK 통합·검증 PoC를 완료하고 자원 제약 환경의 적용 기준 확보

#### 1-3. AI 추론 SDK 개발 및 제품화

회사/기간: 가우디오랩, 2024년

- 배경/과제: Mac·Windows·Mobile CPU, AI Processor, GPU처럼 실행 환경이 다른 타깃에서 추론 SDK의 적용성 확보
- 책임 범위: 사내 머신러닝 추론 SDK를 개발하고 타깃별 미디어 경로와 입출력 방식을 연동
- 핵심 구현: Mac·Windows·Android/iOS CPU SDK의 WebRTC 연동, GAP9 AI Processor 통합, NVIDIA Tegra의 GStreamer Element 통합 수행
- 최적화: 모델 Graph 구현과 PyTorch·ONNX·TensorRT 기반 추론 방식 검토·최적화 수행
- 제품 적용: WebRTC 연동 환경과 GStreamer 기반 NVIDIA Tegra 보드 환경에 SDK를 적용해 제품 동작 검증

#### 1-4. TWS SDK 통합 및 최적화

회사/기간: 가우디오랩, 2021.09 - 2023.12
기여도: 50~100% (프로젝트별 상이)

- 배경/과제: 이기종 TWS DSP의 리소스 제약 속에서 SDK 적용성 확보
- 책임 범위: 타깃별 SDK 기능 개발과 통합 지점·입출력 버퍼 연동 방식을 구현하고, 플랫폼별 동작 차이와 성능 지표 분석
- 핵심 구현: IMU 헤드 트래킹·지연·버퍼 동작 분석, SDK 입출력 버퍼 연동, Fixed-point·SIMD 최적화 수행
- 결과: 이기종 TWS DSP 타깃 통합 버전을 릴리즈하고, Airoha·QCC 일부 타깃에서는 SDK를 제품 탑재해 양산까지 진행

#### 1-5. Android Audio SDK 통합 및 지연 분석

회사/기간: 가우디오랩, 2021.03 - 2021.09
기여도: 80%

- 배경/과제: Android 오디오 경로의 레이어별 지연·기능 제약·유지보수 범위가 달라 SDK 적용 위치에 따른 리스크가 큼
- 책임 범위: Android 플랫폼용 SDK 기능을 개발하고, App·AOSP Framework/Audio HAL·Qualcomm Hexagon DSP 레이어별 지연 유발 구간과 통합 제약 비교
- 핵심 판단: DSP·HAL·Audio Effect별 적용 범위와 제약을 문서화
- 결과: Oboe/ExoPlayer 기반 재생 경로 검증으로 통합 의사결정 기준 확보

### 2. Linux/Android IoT 플랫폼 제품화

회사/기간: 현대에이치티, 2018.09 - 2021.03
기여도: 40~100% (프로젝트별 상이)

- 배경/과제: 로컬 중심 월패드를 해외향 홈 IoT 연동 모델로 전환하면서 장치 제어·서버 API·사용자 기능의 통합 필요
- 책임 범위: 해외향 Linux/Android 월패드 모델의 분석·설계·개발·배포·매뉴얼 작성을 단독 수행
- 핵심 구현: REST/MQTT 데이터 연동, SIP 영상통화, Android Framework·시스템 애플리케이션 기능 개발
- 병목 개선: RS-485 제어·상태 Queue 분리로 다기기 동시 제어의 명령 처리 대기 완화
- 결과: 홈 IoT 플랫폼 연동 안정화와 API Gateway/Push 분리 기반 MSA 전환 참여로 제품 출시 대응

### 3. 멀티플랫폼 개발도구 구축

회사/기간: 에스코어, 2015.08 - 2018.08
기여도: 40~60% (프로젝트별 상이)

- 배경/과제: 여러 OS에서 설치·업데이트·삭제와 패키지 관리 방식이 달라 개발도구 사용 흐름의 일관성 확보 필요
- 책임 범위: Installer/Uninstaller/Package Manager와 공통 유틸리티 개발
- 핵심 구현: Windows·Ubuntu·macOS GUI/CLI의 설치·업데이트·삭제, 패키지·Extension·Repository 관리 기능 구현
- 결과: VS Code Extension으로 Tizen CLI의 프로젝트 생성·빌드·패키징 흐름을 연동해 개발 환경 사용성 개선

## 이전 제품·시스템 개발 경험

### 한국해양기상기술 | Android·Linux 시스템 및 웹 모니터링 구축

회사/기간: 한국해양기상기술, 2013.10 - 2015.07

- 책임 범위: Android 앱 개발, Linux 기반 ROSE 시스템 구축·교육, 웹 모니터링 기능 개발
- Android: 기상·해양 정보 앱의 데이터 파싱·표시와 센서·카메라·갤러리 연동 기능 개발
- Linux·웹: Linux 소스 패키지 설치와 ROSE 작업 스케줄 환경을 구축하고, 로그 파싱·시각화·관리 기능 구현

### 휴맥스 | 상용 셋탑박스 APP/Middleware 개발

회사/기간: 휴맥스, 2009.12 - 2013.10

- 책임 범위: 차량용·블루레이·PVR·IP 셋탑박스 APP/Middleware 기능 개발과 제품별 기능 적용 수행
- 핵심 구현: EPG·Program Info·Menu·Install, 방송 데이터 파싱·관리, AV Control 기능 개발
- 플랫폼 적용: 일본향 전용 Middleware를 공용 Middleware로 이식하고, OIPF JavaScript API와 Android 연동 기능 개발

## 기술 요약

- 핵심 역량: Embedded/Platform Software, SDK Development, System Integration, Middleware
- 최적화: DSP Library, Fixed-point, SIMD, Memory/MIPS Optimization, Latency/Buffer Analysis
- 플랫폼: AAOS (Android Automotive OS), Embedded Linux, Android, RTOS / Bare-metal, ADI SHARC+, Qualcomm SA, Qualcomm Hexagon DSP, Telechips, QCC, Airoha, NVIDIA Tegra X2, GAP9
- 미디어/프레임워크: Audio Weaver, SigmaStudio, WebRTC, GStreamer, Android Audio HAL/Effect
- 품질/릴리즈: 정적 분석, 동적 분석, 단위/통합 테스트 자동화, Jenkins 기반 빌드/배포
