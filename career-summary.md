# 경력기술서 요약

## Senior Embedded / Platform Software Engineer

상용 임베디드 제품과 플랫폼 소프트웨어를 개발해온 16년 경력의 엔지니어입니다. 최근에는 다양한 OS·SoC 환경에서 SDK 개발, 시스템 통합, 성능 분석, 검증·릴리즈를 수행했습니다.

## 회사별 경력 및 주요 프로젝트

### 가우디오랩 (2021.03 - 현재)

오디오 SDK 개발 및 플랫폼 통합

- 배경/과제: OS·SoC와 오디오 입출력 경로가 다른 제품에 공통 SDK를 적용할 수 있도록 기능과 통합 기준 마련
- 책임 범위: 타깃 요구사항을 SDK 기능과 Public API로 구체화하고, 플랫폼별 구현·포팅·검증 수행
- 통합·성능: Android 오디오 레이어와 DSP의 적용 지점을 분석하고, 메모리·연산량·지연·버퍼·호환성 문제를 타깃별로 재현·개선
- 결과: 단위·회귀 테스트와 CI/CD 빌드·패키징·검증 절차로 플랫폼별 적용 기준과 릴리즈 재현성 확보

#### 차량용 내장 앰프 헤드유닛 SDK 개발·포팅 (2026년 - 현재)

- 배경/과제: Qualcomm SA 계열 양산 대상 및 Telechips AAOS 기반의 각 내장 앰프 헤드유닛 환경에서 오디오 SDK의 제품 적용성 확보
- 책임 범위: 개발 PM 역할을 겸하며 타깃별 SDK 기능 개발·포팅, 오디오 경로 통합, 동작 안정화와 검증 수행
- 핵심 구현: 각 헤드유닛의 오디오 경로와 플랫폼 제약을 분석해 SDK 적용 방식 구현
- 튜닝 도구: 전용 제어·파라미터 튜닝 도구를 개발해 헤드유닛 타깃 검증과 튜닝에 활용
- 양산 적용: Qualcomm SA 헤드유닛의 양산 적용을 위한 SDK 개발·포팅과 검증 수행
- 결과: Memory/MIPS·지연·버퍼 이슈를 분석하고 타깃별 검증·릴리즈 절차 수행

#### 차량용 외장 앰프 SDK 통합 및 최적화 (2025년)

- 배경/과제: 외장 앰프 DSP 환경의 연산·메모리 제약 속에서 공통 오디오 SDK의 제품 적용성 확보
- 책임 범위: ADI SHARC+ DSP·Audio Weaver 환경의 SDK 기능 개발·통합 방식과 검증 기준을 정리하고 제품 동작 안정화 수행
- 핵심 구현: Memory/MIPS·지연·버퍼 이슈를 분석하고 자원 제약에 맞춘 최적화 적용
- 튜닝 도구: 전용 제어·파라미터 튜닝 도구를 개발해 외장 앰프 타깃의 검증과 튜닝에 활용
- 결과: 외장 앰프 타깃의 SDK 통합·검증 PoC를 완료하고 자원 제약 환경의 적용 기준 확보

#### AI 추론 SDK 개발 및 제품화 (2024년)

- 배경/과제: Mac·Windows·Mobile CPU, AI Processor, GPU처럼 실행 환경이 다른 타깃에서 추론 SDK의 적용성 확보
- 책임 범위: 사내 머신러닝 추론 SDK를 개발하고 타깃별 미디어 경로와 입출력 방식을 연동
- 핵심 구현: Mac·Windows·Android/iOS CPU SDK의 WebRTC 연동, GAP9 AI Processor 통합, NVIDIA Tegra의 GStreamer Element 통합 수행
- 최적화: 모델 Graph 구현과 PyTorch·ONNX·TensorRT 기반 추론 방식 검토·최적화 수행
- 제품 적용: WebRTC 연동 환경과 GStreamer 기반 NVIDIA Tegra 보드 환경에 SDK를 적용해 제품 동작 검증

#### TWS SDK 통합 및 최적화 (2021.09 - 2023.12)

- 배경/과제: 이기종 TWS DSP의 리소스 제약 속에서 SDK 적용성 확보
- 책임 범위: TWS SDK 통합 프로젝트의 기술 리딩을 맡고, 타깃별 SDK 기능 개발·입출력 버퍼 연동과 플랫폼별 동작·성능 분석 수행
- 핵심 구현: IMU 헤드 트래킹·지연·버퍼 동작 분석, SDK 입출력 버퍼 연동, Fixed-point·SIMD 최적화 수행
- 결과: 이기종 TWS DSP 타깃 통합 버전을 릴리즈하고, Airoha·QCC 일부 타깃에서는 SDK를 제품에 탑재해 양산까지 진행

#### Android Audio SDK 통합 및 지연 분석 (2021.03 - 2021.09)

- 배경/과제: Android 오디오 경로의 레이어별 지연·기능 제약·유지보수 범위가 달라 SDK 적용 위치에 따른 리스크가 큼
- 책임 범위: Android 플랫폼용 SDK 기능을 개발하고, App·AOSP Framework/Audio HAL·Qualcomm Hexagon DSP 레이어별 지연 유발 구간과 통합 제약 비교
- 핵심 판단: DSP·HAL·Audio Effect별 적용 범위와 제약을 문서화
- 결과: Oboe/ExoPlayer 기반 재생 경로 검증으로 통합 의사결정 기준 확보

### 현대에이치티 (2018.09 - 2021.03)

월패드 플랫폼 및 서버 개발

#### 2-1. 해외향 홈 IoT 월패드 제품화 (2020.03 - 2021.03)

- 배경/과제: 로컬 중심 월패드를 해외향 홈 IoT 연동 모델로 전환하면서 장치 제어·서버 API·사용자 기능의 통합 필요
- 책임 범위: 해외향 Linux/Android 월패드 모델의 분석·설계·개발·배포·매뉴얼 작성을 단독 수행
- 핵심 구현: REST/MQTT 데이터 연동, SIP 영상통화, Android Framework·시스템 애플리케이션 기능 개발
- 서버/서비스: Push·방범·시나리오·도어벨 기능 개발과 API Gateway/Push 분리 기반 MSA 전환 참여
- 결과: 홈 IoT 플랫폼 연동을 안정화해 해외향 월패드 모델 출시 대응

#### 2-2. RS-485 다기기 제어 병목 개선 (2018.09 - 2020.03)

- 배경/과제: 여러 기기를 동시에 제어할 때 RS-485 명령 처리에 병목 발생
- 책임 범위: RS-485 장치 제어 흐름의 병목 원인 분석과 처리 구조 개선을 담당
- 핵심 구현: 제어 Queue와 상태 Queue를 분리하는 구조로 변경
- 결과: 다기기 동시 제어에서 명령 처리 대기와 제어 성능 저하 완화

### 에스코어 (2015.08 - 2018.08)

Tizen 개발 플랫폼 도구 개발

- 배경/과제: 여러 OS에서 설치·업데이트·삭제와 패키지 관리 방식이 달라 개발도구 사용 흐름의 일관성 확보 필요
- 책임 범위: Installer/Uninstaller/Package Manager와 공통 유틸리티 개발
- 핵심 구현: Windows·Ubuntu·macOS GUI/CLI의 설치·업데이트·삭제, 패키지·Extension·Repository 관리 기능 구현
- 결과: VS Code Extension으로 Tizen CLI의 프로젝트 생성·빌드·패키징 흐름을 연동해 개발 환경 사용성 개선

### 한국해양기상기술 (2013.10 - 2015.07)

Android 앱·Linux 시스템·웹 모니터링 개발

- 책임 범위: Android 앱 개발, Linux 기반 ROSE 시스템 구축·교육, 웹 모니터링 기능 개발
- Android: 기상·해양 정보 앱의 데이터 파싱·표시와 센서·카메라·갤러리 연동 기능 개발
- Linux·웹: Linux 소스 패키지 설치와 ROSE 작업 스케줄 환경을 구축하고, 로그 파싱·시각화·관리 기능 구현

### 휴맥스 (2009.12 - 2013.10)

상용 셋톱박스 애플리케이션 및 미들웨어 개발

- 책임 범위: 차량용·블루레이·PVR·IP 셋톱박스 APP/Middleware 기능 개발과 제품별 기능 적용 수행
- 핵심 구현: EPG·Program Info·Menu·Install, 방송 데이터 파싱·관리, AV Control 기능 개발
- 플랫폼 적용: 일본향 전용 Middleware를 공용 Middleware로 이식하고, OIPF JavaScript API와 Android 연동 기능 개발

## 주요 기술

제품별 요구사항을 SDK·미들웨어·플랫폼 통합 방식으로 구체화하고, 성능 분석과 검증·릴리즈까지 연결해왔습니다.

- 언어/스크립팅: C/C++, Java, Python, TypeScript, JavaScript, NSIS Script
- Android·임베디드: AAOS, AOSP (App / Framework / Audio HAL), Embedded Linux, RTOS
- DSP: Qualcomm Hexagon, ADI SHARC+, TWS DSP (QCC·Airoha·BES·Bluetrum), Audio Weaver, SigmaStudio
- 미디어 연동: WebRTC, GStreamer Element, Oboe, ExoPlayer
- AI 추론: PyTorch, ONNX, TensorRT, GAP9 AI Processor, NVIDIA Tegra
- 통신·연동: REST, MQTT, SIP, RS-485
- 검증·릴리즈: 단위·회귀 테스트, CI/CD 빌드·패키징, Memory/MIPS·지연·버퍼 분석, 타깃별 SDK 릴리즈
