---
jupytext:
  cell_metadata_filter: all
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0.rc4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Test page break and equation number

using the following `html_context` in conf.py

```
html_context = {
    'page_title': 'Page break',
    'left_header': 'test 1', 
    'center_header': 'Page break test',
    'page_margin_top': 1, # in inches
    'page_margin_bottom': 1, # in inches
    'page_margin_left': 1, # in inches
    'page_margin_right': 1, # in inches
}
```


## Tests

* [page_break](page_break)

* [natural_fill](natural_fill)

* [equation_number](equation_number)

* [equation_ref](equationref)

* [align_equations](align_equations)


(page_break)=
## Test page break

+++

Insert a the following div to get a forced page break:

```
<div class="page-break"></div>
```

<div class="page-break"></div>

+++ 

(natural_fill)=
## Test page fill

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.  Vestibulum convallis, lorem a tempus semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo sit amet elit.


(equation_number)=
##  Test equation number cross reference


$$
\int_\alpha^\beta \cos ( \gamma x ) \, dx
$$ (eq:labelint)

Breaking page here

<div class="page-break"></div>


+++

(equationref)=
## Reference the equation

And here is a reference to equation {eq}`eq:labelint`

(align_equations)=
## Some aligned equations

Q5) From the readings water vapor feedback can be written as:

$$
\begin{align*}
f = \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right) \times \left( \frac{\Delta\mbox{H2O}} {\Delta T} \right )
\end{align*}
$$(eq:h2o)

Which of the following statements is correct?

$$
\begin{align*}
A) \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right ) \mbox{is positive}  \left( \frac{\Delta \mbox{H2O}} {\mbox{ΔT}} \right ) \mbox{is positive} \\
B) \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right ) \mbox{is positive}  \left( \frac{\Delta \mbox{H2O}} {\mbox{ΔT}} \right ) \mbox{is negative} \\
C) \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right ) \mbox{is negative} \left( \frac{\Delta \mbox{H2O}} {\mbox{ΔT}} \right ) \mbox{is positive} \\
D) \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right ) \mbox{is negative} \left( \frac{\Delta \mbox{H2O}} {\mbox{ΔT}} \right ) \mbox{is negative} \\
E) \left( \frac{\Delta R}{\Delta \mbox{H2O}} \right ) \mbox{is negative} \left( \frac{\Delta \mbox{H2O}} {\mbox{ΔT}} \right ) \mbox{is positive} \\
\end{align*}
$$(eq:feedback)


+++ 

```{math}
\begin{align*}
\text{Layer energy equation:} ~~~ & \frac { d E } { d t } = I _ { \downarrow } + I _ { \uparrow }\\
\text{Solar constant:}~~~& S= \frac { S _ { 0 } } { 4 } ( 1 - \alpha )\\
\text{Total grey body flux} ~~~ & I = \varepsilon \sigma T ^ { 4 }\\
&\text{where} ~~~ \sigma = 5.67 \times 10 ^ { - 8 } \mathrm { Wm } ^ { - 2 } \mathrm { K } ^ { - 4 }\nonumber\\
\text{transmissivity tr:}~~~& I _ { \text {transmitted } } = \mathrm { tr } I _ { 0 }\\
\text{reflectity}~ \alpha~~~ & I _ { \text {reflected } } = \alpha I _ { 0 } \\
\text{absorbtivity abs} ~~~ & I _ { \text {absorbed} } = \text{abs} I _ { 0 }\\
\text{Kirchoff's law} ~~ & \varepsilon = \text{abs} \\
\text{$CO_2$ radiative forcing} ~~~& \Delta F = \left(3.8 \mathrm{W} \mathrm{m}^{ - 2 } \right) \frac { \ln ( \text {newp} \operatorname { CO } 2 / \text { origp } \mathrm { CO } 2 ) } { \ln ( 2 ) } \\
\text{Conservation of Energy:}~~~&\alpha \mathrm { I } _ { 0 } + a b s \mathrm { I } _ { 0 } + \mathrm { trI } _ { 0 } = \mathrm { I } _ { 0 }\\
\text{moist static energy:}~~~ & h _ { m } = c _ { p } T + l _ { v } w _ { v } + g z \\
\text{moist adiabatic lapse rate:}~~~&\Gamma = \frac { d T } { d z } = \frac { - g } { c _ { p } + l _ { v } \frac { d w _ { v } } { d T } }\\
\text{hydrostatic balance:}~~~&d p = - \rho g d z \\
\text{mass in a layer in $kg/m^2$:}~~~&M = \int _ { z _ { 1 } } ^ { z _ { 2 } } \rho(z) d z\\
\text{energy in an ocean layer:}~~~&\Delta E=\rho_{w} D c_{w} \Delta T\\
\text{Conservation of energy for layer:}~~~&\frac{d \Delta E}{d t}=\Delta F\\
\text{change of temperature for an ocean layer:}~~~&\frac{d \Delta T}{d t}=\frac{\Delta F}{\rho_{w} c_{w} D}\\
\text{Planck feedback:}~~~&\frac { d I _ { G } } { d T } = \frac { d \left( - \sigma T ^ { 4 } \right) } { d T } = f_{planck} =- 4 \sigma T ^ { 3 } = - 1 / \lambda\\
\text{Conservation of energy with feedback:}~~~&
\frac { \Delta E } { d t } = \Delta F - 4 \sigma T ^ { 3 } \Delta T\\
\text{Climate adjustment to abrupt forcing:}~~~&\Delta T ( t ) = \lambda \Delta F \left( 1 - e ^ { - t / \tau } \right) \\
\text{Climate adjustment timescale:}~~~&\tau = \rho _ { w } c _ { w } D \lambda\\
\text{Climate sensitivity:}~~~&\Delta T = \lambda \Delta F\\
\text{Climage mean temperature budget:}~~~&\rho _ { w } c _ { w } D \frac { d T } { d t } = \Delta F + \sum f _ { n } \Delta T\\
\text{Climate feedback factor:}~~~&f _ { n } = \frac { \Delta R } { \Delta T } = \left( \frac { \Delta R } { \Delta \text { climate } } \right) \left( \frac { \Delta \text { climate } } { \Delta T } \right)\\
\text{Climate sensitivity with feedbacks:}~~~&\lambda = - \frac { 1 } { \sum f _ { n } }
\end{align*}
```
+++ 

# Quiz 2 constants

```{math}
\begin{align*}
&\text{1 ppm = 2.1 Gtonnes Carbon = 7.6 Gtonnes $CO_2$}\\
\sigma  &= 5.67 \times 10 ^ { - 8 } \mathrm { Wm } ^ { - 2 } \mathrm { K } ^ { - 4 }\\
c_p  &= 1004\ J\,kg^{-1}\,K^{-1} \\
c_w  &= 4186\ J\,kg^{-1}\,K^{-1} \\
\rho_w &= 1000\ kg\,m^{-3}\\
l_v &= 2.5 \times 10^6\ J\,kg^{-1}
\end{align*}
```
