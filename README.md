

## Research for the Wake Vortex Project##
> Written with [StackEdit](https://stackedit.io/).
> So we'll base the output parameters on HIRLAM - which is a meterological forecasting model 

| Aircraft Perfomance Parameters  |     Symbol      |  Unit |   Generator      | Encounter|
|----------|:-------------:|:------:|:-------:|---------:|
| Maximum take-off weight |  M | kg  |  Yes       |        No  |
| Wing span |    b   |   m  |      Yes   |      Yes    |
| Aspect ratio | right-aligned |    -  |       No  |    Yes      |
| Wing swap angle | $\Lambda_{c/2}$ |    rad  |       No  | Yes         |

| Parameter |     Symbol      |  Unit |   
|----------|:-------------:|:------:|:-------:|---------:|
|Pressure 0m above ground |  $p_{0}$ | Pa  | 
| Geopotential |    $\Phi$   |   $\frac{m^{2}}{s^{2}}$  |   
| Temperature | T |    K  |      
| Specific humidity | SH |    $\frac{kg}{kg}$  |     
| Relative humidity |  $\psi$ | -  | 
| Turbulence Kinetic Energy |    $\bar{k}$   |   $\frac{m^{2}}{s^{2}}$  |   
| Wind speed - u component | u|    $\frac{m}{s}$  |      
| Wind speed - v component | v |    $\frac{m}{s}$  |   

To describe the decay and vertical transport of the wake vortex the simplified model proposed by De
Visscher is used in this product. The simplified model describes the wake vortex evolution and decay
in two phases for vortices in a stably stratified and weakly turbulent atmospheres. The time-to-demise
which marks the end of the first decay phase and the start of the second decay phase is computed
using the time-to-demise model developed by Sarpkaya .
There are two input parameters for this model. 
The first parameter is the dimensionless Brunt-Vaisala
frequency $N^{∗}$ which relates the properties of the generating aircraft to the atmospheric stability,
described by the Brunt-Vaisala frequency $N$ . 

The second parameter is the dimensionless EDR $\epsilon^{∗}$ which relates the properties of the generating aircraft to the atmospheric turbulence, described by the
EDR $\epsilon$. 

The dimensionless Brunt-Vaisala frequency is defined in the first equation. The dimensionless
EDR is defined in the second equation).
\begin{equation} N ∗ = t _{0} N                             \end{equation}

\begin{equation}\epsilon^{*} = \frac{\epsilon b_{0}}{V^{3}_{0}}
\end{equation}

In these equations the subscript ‘0’ refers to a characteristic scale. There are four characteristic length
scales which are used, namely; the characteristic length $b_{0}$ , velocity $V_{0}$ , circulation $\Gamma_0$ and time $t_0$ .
The characteristic length is defined as the wake vortex spacing, the characteristic circulation is defined
as the initial circulation and the characteristic velocity is defined as the initial descent velocity.  The characteristic time scale is defined as the time it take for the wake vortex to descent a
distance equal to the wake vortex spacing considering the initial descent velocity.

### List of Acronyms 
**ADS-B** Automatic Dependent Surveillance - Broadcast
**AR** Aspect Ratio
**ATC** Air Traffic Control
**ATCO’s** Air Traffic Controllers
**ATFCM** Air Traffic Flow and Capacity Management
**ATM** Air Traffic Management
**BADA** Base of Aircraft Data
**CAT** Clear Air Turbulence
**CPF** Correlated Position File
**CPR** Correlated Position Reports
**CTFM** Current Tactical Flight Model
**DLR** German Aerospace Center
**EDR** Eddy Dissipation Rate
**EVAIR** EUROCONTROL Voluntary ATM Incident Reporting
**FL** Flight Level
**GAT** General Air Traffic
**HIRLAM** High Resolution Local Area Model
**ICAO** International Civil Aviation Organization
**IGE** In Ground Effect
**ISA** International Standard Atmosphere
**KNMI** Royal Netherlands Meteorological Institute
**LES** Large-Eddy Simulations
**LIDAR** Laser Imaging Detection and Ranging
**MAC** Mid-Air Collision
**MLW** Maximum Landing Weight
**MSL** Mean Sea Level
**MTOW** Maximum Take-off Weight
**NLR** Nederlands Luchten Ruimtevaart Institute
**NM** Network Manager
**OEW** Operational Empty Weight
**PRISME** Pan-European Repository of Information Supporting the Management of EATM
**PTCM** Pre-Tactical Conflict Management
**RCR** Roll Control Ratio
**RECAT-EU** Re-categorization of the ICAO Wake Turbulence Separation Minima Europe
**RMC** Rolling Moment Coefficient
**RNP** Required Navigation Performance
**RWC** Reasonable Worst Case
**RVSM** Reduced Vertical Separation Minimum
**SCM** Strategic Conflict Management
**SSR** Secondary Surveillance Radar
**SESAR** Single European Sky ATM Research
**TCM** Tactical Conflict Management
**TKE** Turbulent Kinetic Energy
**TLS** Target Level of Safety
**UCL** Universit Catholique de Louvain
**UTC** Coordinated Universal Time
**VFR** Visual Flight Rules
**WMO** World Meteorological Organization
**WTC** Wake Turbulence Category
**WVE** Wake Vortex Encounter
