# # # import pathlib
# #
# # # current_path = pathlib.Path(__file__).parent.absolute()
# # # print(current_path)
# #
# #
# # # parent_path = current_path.parent
# # # print(parent_path)
# #
# # # data_path = parent_path / "data"
# # # print(data_path)
# #
# # # data_path.mkdir(exist_ok=True)
# # # file_path = data_path / "data.txt"
# #
# # # with open(file_path, "w") as file:
# # #     file.write("Hello, world!")
# #
# # import requests
# #
# # link = 'https://ogmmateryal.eba.gov.tr/calisma-defteri/icerik-goster/44'
# # result_without_redirect = requests.get(link, allow_redirects=False)
# # print(result_without_redirect.status_code)
# # print(result_without_redirect.headers)
# #
# # if result_without_redirect.is_redirect:
# #     print(result_without_redirect.headers["Location"])
# #
# #

# class A:

#     VALUE = 'A VALUE'

#     def __init__(self):
#         print("A value: ", self.VALUE)

# class B(A):
#     VALUE = 'B VALUE'

#     def __init__(self):
#         super().__init__()
#         print("B value: ", self.VALUE)



# b = B()

html = """
<html lang="tr" data-darkreader-mode="dynamic" data-darkreader-scheme="dark" data-darkreader-proxy-injected="true" class="fontawesome-i2svg-active fontawesome-i2svg-complete"><head><style type="text/css">svg:not(:root).svg-inline--fa{overflow:visible;-webkit-box-sizing:content-box;box-sizing:content-box}.svg-inline--fa{display:inline-block;display:var(--fa-display,inline-block);height:1em;overflow:visible;vertical-align:-.125em}.svg-inline--fa.fa-2xs{vertical-align:.1em}.svg-inline--fa.fa-xs{vertical-align:0}.svg-inline--fa.fa-sm{vertical-align:-.0714285705em}.svg-inline--fa.fa-lg{vertical-align:-.2em}.svg-inline--fa.fa-xl{vertical-align:-.25em}.svg-inline--fa.fa-2xl{vertical-align:-.3125em}.svg-inline--fa.fa-pull-left{margin-right:.3em;margin-right:var(--fa-pull-margin,.3em);width:auto}.svg-inline--fa.fa-pull-right{margin-left:.3em;margin-left:var(--fa-pull-margin,.3em);width:auto}.svg-inline--fa.fa-li{width:2em;width:var(--fa-li-width,2em);top:.25em}.svg-inline--fa.fa-fw{width:1.25em;width:var(--fa-fw-width,1.25em)}.fa-layers svg.svg-inline--fa{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}.fa-layers-counter,.fa-layers-text{display:inline-block;position:absolute;text-align:center}.fa-layers{display:inline-block;height:1em;position:relative;text-align:center;vertical-align:-.125em;width:1em}.fa-layers svg.svg-inline--fa{-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-text{left:50%;top:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-counter{background-color:#ff253a;background-color:var(--fa-counter-background-color,#ff253a);border-radius:1em;border-radius:var(--fa-counter-border-radius,1em);-webkit-box-sizing:border-box;box-sizing:border-box;color:#fff;color:var(--fa-inverse,#fff);line-height:1;line-height:var(--fa-counter-line-height,1);max-width:5em;max-width:var(--fa-counter-max-width,5em);min-width:1.5em;min-width:var(--fa-counter-min-width,1.5em);overflow:hidden;padding:.25em .5em;padding:var(--fa-counter-padding,.25em .5em);right:0;right:var(--fa-right,0);text-overflow:ellipsis;top:0;top:var(--fa-top,0);-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform:scale(var(--fa-counter-scale,.25));transform:scale(var(--fa-counter-scale,.25));-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-bottom-right{bottom:0;bottom:var(--fa-bottom,0);right:0;right:var(--fa-right,0);top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:bottom right;transform-origin:bottom right}.fa-layers-bottom-left{bottom:0;bottom:var(--fa-bottom,0);left:0;left:var(--fa-left,0);right:auto;top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:bottom left;transform-origin:bottom left}.fa-layers-top-right{top:0;top:var(--fa-top,0);right:0;right:var(--fa-right,0);-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-top-left{left:0;left:var(--fa-left,0);right:auto;top:0;top:var(--fa-top,0);-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform:scale(var(--fa-layers-scale,.25));transform:scale(var(--fa-layers-scale,.25));-webkit-transform-origin:top left;transform-origin:top left}.fa-1x{font-size:1em}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-6x{font-size:6em}.fa-7x{font-size:7em}.fa-8x{font-size:8em}.fa-9x{font-size:9em}.fa-10x{font-size:10em}.fa-2xs{font-size:.625em;line-height:.1em;vertical-align:.225em}.fa-xs{font-size:.75em;line-height:.0833333337em;vertical-align:.125em}.fa-sm{font-size:.875em;line-height:.0714285718em;vertical-align:.0535714295em}.fa-lg{font-size:1.25em;line-height:.05em;vertical-align:-.075em}.fa-xl{font-size:1.5em;line-height:.0416666682em;vertical-align:-.125em}.fa-2xl{font-size:2em;line-height:.03125em;vertical-align:-.1875em}.fa-fw{text-align:center;width:1.25em}.fa-ul{list-style-type:none;margin-left:2.5em;margin-left:var(--fa-li-margin,2.5em);padding-left:0}.fa-ul>li{position:relative}.fa-li{left:calc(2em * -1);left:calc(var(--fa-li-width,2em) * -1);position:absolute;text-align:center;width:2em;width:var(--fa-li-width,2em);line-height:inherit}.fa-border{border-color:#eee;border-color:var(--fa-border-color,#eee);border-radius:.1em;border-radius:var(--fa-border-radius,.1em);border-style:solid;border-style:var(--fa-border-style,solid);border-width:.08em;border-width:var(--fa-border-width,.08em);padding:.2em .25em .15em;padding:var(--fa-border-padding,.2em .25em .15em)}.fa-pull-left{float:left;margin-right:.3em;margin-right:var(--fa-pull-margin,.3em)}.fa-pull-right{float:right;margin-left:.3em;margin-left:var(--fa-pull-margin,.3em)}.fa-beat{-webkit-animation-name:fa-beat;animation-name:fa-beat;-webkit-animation-delay:0;animation-delay:0;-webkit-animation-delay:var(--fa-animation-delay,0);animation-delay:var(--fa-animation-delay,0);-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:ease-in-out;animation-timing-function:ease-in-out;-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}.fa-fade{-webkit-animation-name:fa-fade;animation-name:fa-fade;-webkit-animation-delay:0;animation-delay:0;-webkit-animation-delay:var(--fa-animation-delay,0);animation-delay:var(--fa-animation-delay,0);-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:cubic-bezier(.4,0,.6,1);animation-timing-function:cubic-bezier(.4,0,.6,1);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}.fa-flash{-webkit-animation-name:fa-flash;animation-name:fa-flash;-webkit-animation-delay:0;animation-delay:0;-webkit-animation-delay:var(--fa-animation-delay,0);animation-delay:var(--fa-animation-delay,0);-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:cubic-bezier(.4,0,.6,1);animation-timing-function:cubic-bezier(.4,0,.6,1);-webkit-animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1));animation-timing-function:var(--fa-animation-timing,cubic-bezier(.4,0,.6,1))}.fa-flip{-webkit-animation-name:fa-flip;animation-name:fa-flip;-webkit-animation-delay:0;animation-delay:0;-webkit-animation-delay:var(--fa-animation-delay,0);animation-delay:var(--fa-animation-delay,0);-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:ease-in-out;animation-timing-function:ease-in-out;-webkit-animation-timing-function:var(--fa-animation-timing,ease-in-out);animation-timing-function:var(--fa-animation-timing,ease-in-out)}.fa-spin{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-delay:0;animation-delay:0;-webkit-animation-delay:var(--fa-animation-delay,0);animation-delay:var(--fa-animation-delay,0);-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:2s;animation-duration:2s;-webkit-animation-duration:var(--fa-animation-duration,2s);animation-duration:var(--fa-animation-duration,2s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:linear;animation-timing-function:linear;-webkit-animation-timing-function:var(--fa-animation-timing,linear);animation-timing-function:var(--fa-animation-timing,linear)}.fa-spin-reverse{--fa-animation-direction:reverse}.fa-pulse,.fa-spin-pulse{-webkit-animation-name:fa-spin;animation-name:fa-spin;-webkit-animation-direction:normal;animation-direction:normal;-webkit-animation-direction:var(--fa-animation-direction,normal);animation-direction:var(--fa-animation-direction,normal);-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-duration:var(--fa-animation-duration,1s);animation-duration:var(--fa-animation-duration,1s);-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-iteration-count:var(--fa-animation-iteration-count,infinite);animation-iteration-count:var(--fa-animation-iteration-count,infinite);-webkit-animation-timing-function:steps(8);animation-timing-function:steps(8);-webkit-animation-timing-function:var(--fa-animation-timing,steps(8));animation-timing-function:var(--fa-animation-timing,steps(8))}@media (prefers-reduced-motion:reduce){.fa-beat,.fa-fade,.fa-flash,.fa-flip,.fa-pulse,.fa-spin,.fa-spin-pulse{-webkit-animation-delay:-1ms;animation-delay:-1ms;-webkit-animation-duration:1ms;animation-duration:1ms;-webkit-animation-iteration-count:1;animation-iteration-count:1;-webkit-transition-delay:0s;transition-delay:0s;-webkit-transition-duration:0s;transition-duration:0s}}@-webkit-keyframes fa-beat{0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(1.25);transform:scale(1.25);-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}@keyframes fa-beat{0%,90%{-webkit-transform:scale(1);transform:scale(1)}45%{-webkit-transform:scale(1.25);transform:scale(1.25);-webkit-transform:scale(var(--fa-beat-scale,1.25));transform:scale(var(--fa-beat-scale,1.25))}}@-webkit-keyframes fa-fade{50%{opacity:.4;opacity:var(--fa-fade-opacity,.4)}}@keyframes fa-fade{50%{opacity:.4;opacity:var(--fa-fade-opacity,.4)}}@-webkit-keyframes fa-flash{0%,100%{opacity:.4;opacity:var(--fa-flash-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(1.125);transform:scale(1.125);-webkit-transform:scale(var(--fa-flash-scale,1.125));transform:scale(var(--fa-flash-scale,1.125))}}@keyframes fa-flash{0%,100%{opacity:.4;opacity:var(--fa-flash-opacity,.4);-webkit-transform:scale(1);transform:scale(1)}50%{opacity:1;-webkit-transform:scale(1.125);transform:scale(1.125);-webkit-transform:scale(var(--fa-flash-scale,1.125));transform:scale(var(--fa-flash-scale,1.125))}}@-webkit-keyframes fa-flip{50%{-webkit-transform:rotate3d(0,1,0,-180deg);transform:rotate3d(0,1,0,-180deg);-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}@keyframes fa-flip{50%{-webkit-transform:rotate3d(0,1,0,-180deg);transform:rotate3d(0,1,0,-180deg);-webkit-transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg));transform:rotate3d(var(--fa-flip-x,0),var(--fa-flip-y,1),var(--fa-flip-z,0),var(--fa-flip-angle,-180deg))}}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.fa-rotate-90{-webkit-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-webkit-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-webkit-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-webkit-transform:scale(-1,1);transform:scale(-1,1)}.fa-flip-vertical{-webkit-transform:scale(1,-1);transform:scale(1,-1)}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{-webkit-transform:scale(-1,-1);transform:scale(-1,-1)}.fa-rotate-by{-webkit-transform:rotate(none);transform:rotate(none);-webkit-transform:rotate(var(--fa-rotate-angle,none));transform:rotate(var(--fa-rotate-angle,none))}.fa-stack{display:inline-block;vertical-align:middle;height:2em;position:relative;width:2.5em}.fa-stack-1x,.fa-stack-2x{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0;z-index:auto;z-index:var(--fa-stack-z-index,auto)}.svg-inline--fa.fa-stack-1x{height:1em;width:1.25em}.svg-inline--fa.fa-stack-2x{height:2em;width:2.5em}.fa-inverse{color:#fff;color:var(--fa-inverse,#fff)}.fa-sr-only,.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}.fa-sr-only-focusable:not(:focus),.sr-only-focusable:not(:focus){position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}.svg-inline--fa .fa-primary{fill:currentColor;fill:var(--fa-primary-color,currentColor);opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa .fa-secondary{fill:currentColor;fill:var(--fa-secondary-color,currentColor);opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-primary{opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-secondary{opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa mask .fa-primary,.svg-inline--fa mask .fa-secondary{fill:#000}.fa-duotone.fa-inverse,.fad.fa-inverse{color:#fff;color:var(--fa-inverse,#fff)}</style><style class="darkreader darkreader--sync" media="screen"></style><style class="darkreader darkreader--fallback" media="screen"></style><style class="darkreader darkreader--text" media="screen"></style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, img.Wirisformula, a[data-testid="headerMediumLogo"]>svg, .d2l-navigation-link-image-container, .d2l-iframe-loading-container {
    filter: invert(100%) hue-rotate(180deg) contrast(90%) !important;
}</style><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}
[data-darkreader-inline-bg] {
  background: var(--darkreader-inline-bg) !important;
}
[data-darkreader-inline-border-short] {
  border: var(--darkreader-inline-border-short) !important;
}
[data-darkreader-inline-border-bottom-short] {
  border-bottom: var(--darkreader-inline-border-bottom-short) !important;
}
[data-darkreader-inline-border-left-short] {
  border-left: var(--darkreader-inline-border-left-short) !important;
}
[data-darkreader-inline-border-right-short] {
  border-right: var(--darkreader-inline-border-right-short) !important;
}
[data-darkreader-inline-border-top-short] {
  border-top: var(--darkreader-inline-border-top-short) !important;
}
[data-darkreader-inline-invert] {
    filter: invert(100%) hue-rotate(180deg);
}</style><style class="darkreader darkreader--variables" media="screen">:root {
   --darkreader-neutral-background: var(--darkreader-background-ffffff, #181a1b);
   --darkreader-neutral-text: var(--darkreader-text-000000, #e8e6e3);
   --darkreader-selection-background: var(--darkreader-background-0060d4, #004daa);
   --darkreader-selection-text: var(--darkreader-text-ffffff, #e8e6e3);
}</style><style class="darkreader darkreader--root-vars" media="screen"></style><style class="darkreader darkreader--user-agent" media="screen">@layer {
html {
    background-color: var(--darkreader-background-ffffff, #181a1b) !important;
}
html {
    color-scheme: dark !important;
}
iframe {
    color-scheme: dark !important;
}
html, body {
    background-color: var(--darkreader-background-ffffff, #181a1b);
}
html, body {
    border-color: var(--darkreader-border-4c4c4c, #736b5e);
    color: var(--darkreader-text-000000, #e8e6e3);
}
a {
    color: var(--darkreader-text-0040ff, #3391ff);
}
table {
    border-color: var(--darkreader-border-808080, #545b5e);
}
mark {
    color: var(--darkreader-text-000000, #e8e6e3);
}
::placeholder {
    color: var(--darkreader-text-a9a9a9, #b2aba1);
}
input:-webkit-autofill,
textarea:-webkit-autofill,
select:-webkit-autofill {
    background-color: var(--darkreader-background-faffbd, #404400) !important;
    color: var(--darkreader-text-000000, #e8e6e3) !important;
}
::selection {
    background-color: var(--darkreader-background-0060d4, #004daa) !important;
    color: var(--darkreader-text-ffffff, #e8e6e3) !important;
}
::-moz-selection {
    background-color: var(--darkreader-background-0060d4, #004daa) !important;
    color: var(--darkreader-text-ffffff, #e8e6e3) !important;
}
}</style>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" href="/assets/img/favicon.ico">
    <link rel="stylesheet" href="/assets/css/bootstrap.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="/assets/css/font-awesome.all.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="/assets/css/style.css"><style class="darkreader darkreader--cors" media="screen">* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Roboto', sans-serif;
}

body {
    min-height: 600px;
}

html {
    scroll-behavior: smooth;
}

a {
    text-decoration: none;
}

.blink {
    animation: blinker 1s linear infinite;
}

@keyframes blinker {
    50% {
        opacity: 0;
    }
}

#scrollUp {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    font-size: 18px;
    border: none;
    outline: none;
    background-color: rgb(218, 41, 28);
    color: white;
    cursor: pointer;
    padding: 5px 10px;
    border-radius: 4px;
    transition: all 0.3s ease;
}

#scrollUp:hover {
    background-color: #555;
}

.section-title {
    margin-bottom: 2.5rem;
    text-align: center;
}

.section-title h2 {
    font-size: 25px;
    font-weight: 600;
    position: relative;
}

.section-title h2::after {
    content: "";
    margin-top: 0.35rem;
    position: absolute;
    top: 100%;
    left: 48.5%;
    background-color: rgb(218, 41, 28);
    height: 3px;
    width: 35px;
}

hr {
    background: #a5a5a5;
}

.form-control:focus{
    box-shadow: none;
    outline: 0;
    border-color: #23272b;
}

@-webkit-keyframes sticky-animation {
    0% {
        opacity: 0;
        -webkit-transform: translateY(-100%);
    }

    100% {
        opacity: 1;
        -webkit-transform: translateY(0);
    }
}

@keyframes sticky-animation {
    0% {
        opacity: 0;
        transform: translateY(-100%);
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.sticky {
    position: fixed;
    top: 0 !important;
    background-color: #fff;
    left: 0;
    right: 0;
    z-index: 1000;
    width: 100%;
    -webkit-animation-duration: .5s;
    animation-duration: .5s;
    -webkit-animation-name: sticky-animation;
    animation-name: sticky-animation;
    -webkit-animation-timing-function: ease-out;
    animation-timing-function: ease-out;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
}

.sticky .main-logo img {
    width: 200px !important;
}

.sticky .main-menu-link li a {
    font-size: 15.5px !important;
}

.sticky .ana-menu .sub-menu li a {
    font-size: 13px !important;
}

.offcanvas-end {
    border-left: 0 !important;
    background-color: rgb(243, 243, 243);
}

.offcanvas-end .offcanvas-header {
    border-bottom: 1px solid rgb(206, 206, 206);
    padding: 0;
}

.offcanvas-end .offcanvas-header .input-group {
    padding: 1rem;
}

.offcanvas-end .offcanvas-header .offcanvas-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem;
    border-bottom: 1px solid rgb(206, 206, 206);
}

.offcanvas-end .offcanvas-header h5 {
    margin-bottom: 0;
    color: rgba(0, 0, 0, 0.5);
    font-size: 16px;
}

.offcanvas-end .offcanvas-body {
    padding: 0;
}

.offcanvas-end .offcanvas-body .offcanvas-list {
    padding: 1rem 1rem 1rem 2rem;
    list-style-type: square;
}

.offcanvas-end .offcanvas-body .offcanvas-list li {
    border-bottom: 1px solid rgb(206, 206, 206);
}

.offcanvas-end .offcanvas-body .offcanvas-list li:last-child {
    border-bottom: 0;
}

.offcanvas-end .offcanvas-body .offcanvas-list li a {
    color: rgba(0, 0, 0, 0.95);
    font-size: 16px;
    font-weight: 400;
    margin: 0;
    display: block;
    padding: 10px 10px 10px 10px;
}

.img-hover-zoom {
    overflow: hidden;
    width: 100%;
}

.img-hover-zoom img {
    transition: transform 0.8s ease;
}

.img-hover-zoom:hover img {
    transform: scale(1.15);
}





#ogm-head .ogm-top-menu {
    background-color: #23272b;
    color: #fff;
    padding: 0.35rem 0;
}

#ogm-head .ogm-top-menu .ogm-head-social {
    list-style: none;
    margin-bottom: 0;
    padding-left: 0.2rem;
    display: flex;
    align-items: center;
}

#ogm-head .ogm-top-menu .ogm-head-social li {
    margin-right: 1rem;
}

#ogm-head .ogm-top-menu .ogm-head-social li:last-child {
    margin-right: 0;
}

#ogm-head .ogm-top-menu .ogm-head-social li a {
    color: #fff;
}

#ogm-head .ogm-top-menu .mobil-app-icon {
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

#ogm-head .ogm-top-menu .mobil-app-icon .mobil-app-icon-text {
    margin-right: 0.7rem;
}

#ogm-head .ogm-top-menu .mobil-app-icon .mobil-app-icon-text span {
    font-size: 15px;
}

#ogm-head .ogm-top-menu .mobil-app-icon .mobil-app-icon-item {
    margin-right: 0.75rem;
}

#ogm-head .ogm-top-menu .mobil-app-icon .mobil-app-icon-item:last-child {
    margin-right: 0;
}

#ogm-head .ogm-top-menu .mobil-app-icon .mobil-app-icon-item a {
    background-color: rgb(218, 41, 28);
    padding: 0.2rem 0.4rem;
    border-radius: 5px;
    color: #fff;
    font-size: 21px;
}


#ogm-head .ogm-main-menu {
    padding: 0.5rem 0;
    box-shadow: 0 3px 5px 0 rgb(0 0 0 / 4%);
}

#ogm-head .ogm-main-menu .main-menu-items {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

#ogm-head .ogm-main-menu .main-menu-items .main-logo img {
    width: 220px;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link {
    list-style: none;
    display: flex;
    align-items: center;
    margin-bottom: 0;
    padding-left: 0;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link .dropdown-toggle::after {
    color: rgba(0, 0, 0, .5) !important;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link li {
    margin-right: 1.9rem;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link li:last-child {
    margin-right: 0;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link li a {
    color: #000;
    font-size: 15.5px;
    font-weight: 500;
    letter-spacing: -1px;
}

#ogm-head .ogm-main-menu .main-menu-items .main-menu-link li a:hover {
    color: rgb(218, 41, 28);
}


#ogm-head .ogm-main-menu .main-menu-bar {
    width: 33px;
    height: 23px;
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    -transform: rotate(0deg);
    transition: 0.5s ease-in-out;
    cursor: pointer;
    display: none;
}

#ogm-head .ogm-main-menu .main-menu-bar span {
    display: block;
    position: absolute;
    height: 3px;
    width: 33px;
    background: rgb(36, 36, 36);
    opacity: 1;
    left: 0;
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    -transform: rotate(0deg);
    transition: 0.25s ease-in-out;
}

#ogm-head .ogm-main-menu .main-menu-bar span:nth-child(1) {
    top: 0px;
    -ms-transform-origin: left center;
    transform-origin: left center;
}

#ogm-head .ogm-main-menu .main-menu-bar span:nth-child(2) {
    top: 8px;
    -ms-transform-origin: left center;
    transform-origin: left center;
}

#ogm-head .ogm-main-menu .main-menu-bar span:nth-child(3) {
    top: 16px;
    -ms-transform-origin: left center;
    transform-origin: left center;
}


#ogm-head .ogm-main-menu-bottom {
    padding: 0.2rem 0;
    box-shadow: 0 3px 5px 0 rgb(0 0 0 / 4%);
}

.mobile-menu-bottom {
    padding: 1.15rem 0;
}

.mobile-menu-bottom .row {
    --bs-gutter-x: 2.65rem;
}

.mobile-menu-bottom .form-select {
    border-radius: 12px;
    font-size: 15px;
    letter-spacing: -1px;
}

select:focus {
    outline: 0;
}

#ogm-head .ogm-main-menu-bottom .main-menu-bottom-link {
    list-style: none;
    margin-bottom: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 0;
}

#ogm-head .ogm-main-menu-bottom .main-menu-bottom-link li a {
    margin-right: 2.5rem;
}

#ogm-head .ogm-main-menu-bottom .main-menu-bottom-link li:last-child a {
    margin-right: 0;
}

#ogm-head .ogm-main-menu-bottom .main-menu-bottom-link li a {
    color: #000;
    font-weight: 600;

    font-size: 17px;
    letter-spacing: -1px;
}

.link-underline {
    position: relative;
    line-height: 50px;
    display: inline-block;
}

.link-underline::after {
    content: "";
    width: 0;
    height: 2px;
    background: #000;
    position: absolute;
    top: calc(100% - 2px);
    left: 50%;
    transition: all .2s;
}

.ana-menu:hover .link-underline {
    border-bottom-width: 0;
    color: #000;
}

.ana-menu:hover .link-underline::after {
    left: 0%;
    width: 100%;
}

.ana-menu {
    position: relative;
}

.ana-menu .sub-menu {
    text-align: left;
    position: absolute;
    visibility: hidden;
    display: block;
    opacity: 0;
    line-height: 14px;
    right: 0;
    border-top: 3px solid transparent;
    top: 130%;
    -webkit-box-shadow: 0 6px 12px rgb(0 0 0 / 18%);
    box-shadow: 0 6px 12px rgb(0 0 0 / 18%);
    transition: all .2s ease;
    z-index: 99;
    background-color: #fff;
    width: 300px;
    list-style: none;
    padding-left: 0;
}

.ana-menu .sub-menu li {
    border-bottom: 1px solid rgb(231, 231, 231);
    margin-right: 0 !important;
}

.ana-menu .sub-menu li a {
    color: #000;
    font-size: 14px;
    font-weight: 500;
    margin: 0;
    display: block;
    padding: 12.5px 10px 12.5px 10px;
}

.ana-menu .sub-menu li a:hover {
    font-weight: 600;
}

.ana-menu:hover .sub-menu {
    opacity: 1 !important;
    visibility: visible !important;
    border-color: rgb(218, 41, 28);
}

.has-submenu {
    position: relative;
}

.has-submenu::after {
    content: "➞";
    position: absolute;
    background-color: transparent;
    right: 12px;
    top: 8px;
    display: inline-block;
    font-size: 15px !important;
    margin-left: 4px;
}

.has-submenu .sub-menu-2 {
    text-align: left;
    position: absolute;
    visibility: hidden;
    display: block;
    opacity: 0;
    line-height: 14px;
    left: 100%;
    border-top: 1px solid rgb(231, 231, 231);
    top: 0;
    -webkit-box-shadow: 0 6px 12px rgb(0 0 0 / 18%);
    box-shadow: 0 6px 12px rgb(0 0 0 / 18%);
    transition: all .2s ease;
    z-index: 99;
    background-color: #f8f9fa;
    width: 250px;
    list-style: none;
    padding-left: 0;
}

.has-submenu .sub-menu-2 li {
    border-bottom: 1px solid rgb(231, 231, 231);
}

.has-submenu .sub-menu-2 li a {
    color: #000;
    font-size: 14px;
    font-weight: 500;
    margin: 0;
    display: block;
    padding: 10px 10px 10px 10px;
}

.has-submenu:hover .sub-menu-2 {
    opacity: 1 !important;
    visibility: visible !important;
}



.head-slider .mobile-slide {
    display: none;
}

.head-slider .swiper-pagination-bullet {
    width: 38px;
    height: 13px;
    border-radius: 0;
}

.head-slider .swiper-pagination-bullet-active {
    background: rgb(218, 41, 28);
}

.head-slider img {
    width: 100%;
}


.ogm-books .row {
    --bs-gutter-x: 1.85rem;
}

.ogm-books .ogm-books-img {
    position: relative;
    margin-bottom: 0 !important;
    border-radius: 20px;
}

.ogm-books .ogm-books-img img {
    width: 100%;
    border-radius: 20px;
}

.ogm-books .ogm-books-img .ogm-books-img-color {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    height: 100%;
    width: 100%;
    background: rgb(95, 95, 95);
    opacity: 0.4;
    border-radius: 20px;
}

.ogm-books .ogm-books-img:hover .ogm-books-img-color {
    opacity: 0.6;
}

.ogm-books .ogm-books-img .ogm-books-head {
    position: absolute;
    top: 33%;
    left: 0;
    right: 0;
    color: #fff;
    text-transform: uppercase;
    text-align: center;
    padding: 0 1.85rem;
}

.ogm-books .ogm-books-img .ogm-books-head .books-number {
    border-right: 2px solid rgb(218, 41, 28);
    border-left: 2px solid rgb(218, 41, 28);
    border-bottom: 2px solid rgb(218, 41, 28);
    color: #fff;
    padding: 0.15rem 0.50rem;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: -1px;
    text-transform: capitalize;
}
.ogm-books .ogm-books-img .ogm-books-head .books-number .number-text{
    font-weight: 500;
}

.ogm-books .ogm-books-img .ogm-books-head .books-number-2 {
    background-color: #fff;
    color: rgb(218, 41, 28);
    padding: 0.25rem 0.60rem;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: -1px;
    border-radius: 20px;
}

.ogm-books .ogm-books-img .ogm-books-head h2 {
    font-size: 28px;
    font-weight: 600;
    margin-top: 0.75rem;
}

.ogm-books .ogm-books-img .ogm-books-head p {
    font-size: 13px;
    margin-bottom: 0;
    margin-top: 1rem;
    letter-spacing: 1px;
    opacity: 0;
    text-transform: capitalize;
    color: rgb(238, 238, 238);
    -webkit-transform: translate3d(0, -10px, 0);
    transform: translate3d(0, -10px, 0);
    -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
    transition: opacity 0.35s, transform 0.35s;
}

.ogm-books .ogm-books-img .ogm-books-head h3 {
    font-size: 18px;
    line-height:28px;
    font-weight: 600;
    margin-top: 0.75rem;
}

.ogm-books-img figcaption {
    color: #fff;
    text-transform: uppercase;
    font-size: 1.25em;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    padding: 1em;
}

.ogm-books-img figcaption,
.ogm-books-img figcaption>a {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.ogm-books-img figcaption::before {
    position: absolute;
    content: '';
    top: 36px;
    right: 7px;
    bottom: 30px;
    left: 7px;
    border-top: 1px solid #fff;
    border-bottom: 1px solid #fff;
    opacity: 0;
    -webkit-transform: scale(0, 1);
    transform: scale(0, 1);
    -webkit-transform-origin: 0 0;
    transform-origin: 0 0;
    -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
    transition: opacity 0.35s, transform 0.35s;

}

.ogm-books-img figcaption::after {
    position: absolute;
    content: '';
    top: 15px;
    right: 15px;
    bottom: 15px;
    left: 17px;
    border-right: 1px solid #fff;
    border-left: 1px solid #fff;
    opacity: 0;
    -webkit-transition: opacity 0.35s, -webkit-transform 0.35s;
    transition: opacity 0.35s, transform 0.35s;
    -webkit-transform: scale(1, 0);
    transform: scale(1, 0);
    -webkit-transform-origin: 100% 0;
    transform-origin: 100% 0;
}

.ogm-books-img:hover figcaption::before,
.ogm-books-img:hover figcaption::after {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
}

.ogm-books-img:hover figcaption p {
    opacity: 1 !important;
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    -webkit-transition-delay: 0.15s;
    transition-delay: 0.15s;
}



.ogm-statistics {
    background-color: #f6f6f6;
}

.ogm-statistics .row {
    --bs-gutter-x: 4rem;
}

.ogm-statistics .statistics-icon {
    margin-bottom: 0.15rem;
}

.ogm-statistics .statistics-icon svg {
    font-size: 32px;
    background: #eeeeee;
    color: #23272b;
    border: 1px solid #d3d3d3;
    padding: 0.85rem 0.95rem;
    border-radius: 10px;
}

.ogm-statistics .statistics-head span {
    font-size: 26px;
    color: rgb(218, 41, 28);
    letter-spacing: -1px;
    font-family: 'Roboto Mono', monospace;
}

.ogm-statistics .statistics-desc {
    line-height: 1.15rem;
}

.ogm-statistics .statistics-desc span {
    color: rgb(44, 44, 44);
    font-size: 14px;
    font-weight: 500;
}


.breadcrumb-area {
    border-bottom: 1px solid rgb(236, 236, 236);
}

.breadcrumb {
    align-items: center;
}

.breadcrumb li a {
    color: #000;
}

.breadcrumb-item.active {
    color: rgb(218, 41, 28);
    font-size: 17px;
}


.breadcrumb-area .test-button .btn {
    background-color: #fff;
    color: #23272b;
    border: 1px solid #23272b;
    border-radius: 12px;
    letter-spacing: -1px;
    padding: 0.35rem 2.5rem;
    white-space: nowrap;
}

.breadcrumb-area .test-button .btn:hover {
    background-color: #23272b;
    color: #fff;
    border: 1px solid #fff;
}


.ogm-units .ogm-units-head {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 1.85rem;
    position: relative;
}

.ogm-units .ogm-units-head::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    background: rgb(218, 41, 28);
    width: 45px;
    height: 2px;
}

.ogm-units .ogm-units-action-button {
    display: flex;
    justify-content: flex-end;
}

.ogm-units .ogm-units-action-button .btn {
    background-color: #fff;
    color: rgb(218, 41, 28);
    border: 1px solid rgb(218, 41, 28);
    border-radius: 12px;
    letter-spacing: -1px;
    padding: 0.35rem 2.5rem;
    white-space: nowrap;
}

.ogm-units .ogm-units-action-button .btn:hover {
    background-color: rgb(218, 41, 28);
    color: #fff;
    border: 1px solid #fff;
}

.ogm-units .ogm-units-icon {
    margin-bottom: 0.2rem;
    text-align: center;
    font-size: 29px;
}

.ogm-units .ogm-units-question-head h4 {
    margin-bottom: 0;
    font-size: 16px;
    font-weight: 500;
    text-align: center;
}

.ogm-units .test-item {
    text-align: center;
}

.ogm-units .test-item a {
    color: #23272b;
    background-color: rgb(250, 250, 250);
    border: 1px solid rgb(236, 236, 236);
    font-size: 14px;
    padding: 0.7rem 0;
    border-radius: 8px;
    display: block;
    transition: all .1s ease;
}

.ogm-units .test-item a:hover {
    background-color: rgb(218, 41, 28);
    color: #fff;
    border-color: rgb(218, 41, 28);
}

.ogm-units .nav-pills .nav-item {
    text-align: center;
}

.ogm-units .nav-pills .nav-link {
    color: #23272b;
    border-radius: 0;
    padding: 1.05rem 2.25rem 1.45rem 2.25rem;
    border-radius: 12px;
    display: inline-block;
}

.ogm-units .nav-pills .nav-link.active {
    background-color: rgb(218, 41, 28);
    color: #fff;
}

.ogm-units .question-number-section {
    margin-top: 2.65rem;
    background-color: #fff;
    box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;
    padding: 1rem 1.5rem 2rem 1.5rem;
}

.ogm-units .question-number-section .question-number-section-head {
    font-size: 20px;
    letter-spacing: -1px;
    font-weight: 500;
}

.ogm-units .question-number-section .question-number-section-note {
    margin-top: 0.85rem;
    font-size: 15px;
}

.ogm-units .question-number-section .question-number-box .question-number-head {
    font-size: 16px;
    letter-spacing: -1px;
    margin-bottom: 0.25rem;
}

.ogm-units .form-check-input:checked {
    background-color: rgb(218, 41, 28);
    border-color: rgb(218, 41, 28);
}

.ogm-units .units-Select {
    margin-left: -32px;
    list-style-type: none;
}

.ogm-units .units-all-select {
    margin-bottom: 1.15rem;
    position: relative;
}

.ogm-units .units-all-select::after {
    content: "";
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 260px;
    height: 1px;
    background-color: rgb(218, 41, 28);
}

.ogm-units .units-Select .units-Select-item {
    margin-bottom: 1.65rem;
    position: relative;
}

.ogm-units .units-Select .units-Select-item::after {
    content: "";
    position: absolute;
    bottom: -12px;
    left: 0;
    width: 260px;
    height: 1px;
    background-color: rgb(218, 41, 28);
}

.ogm-units .units-Select .last-select-item::after {
    content: none !important;
}

.ogm-units .units-Select .units-Select-item .units-Select-item-details {
    list-style: none;
    margin-top: 0.25rem;
    margin-bottom: 0.5rem;
}


.ogm-test .ogm-test-head {
    font-size: 20px;
    font-weight: 600;
    position: relative;
}

.ogm-test .ogm-test-head::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    background: rgb(218, 41, 28);
    width: 45px;
    height: 2px;
}
.ogm-test .nextQuestionButton{
    text-align: right;
}
.ogm-test .nextQuestionButton a{
    background-color: #fff;
    color: rgb(218, 41, 28);
    border: 1px solid rgb(218, 41, 28);
    padding: 0.3rem 0.8rem;
    border-radius: 8px;
    transition: all .1s;
}
.ogm-test .nextQuestionButton a:hover{
    background-color: rgb(218, 41, 28);
    color: #fff;
}


[data-progress] {
    width: 30px;
    height: 15px;
    border-radius: 180px 180px 0 0;
    position: relative;
    overflow: hidden;
    background: #c2c2c2;
}

[data-progress]:before {
    content: attr(data-progress);
    display: block;
    margin: 18px;
    background: white;
    text-align: center;
    font-size: 30px;
    line-height: 50px;
    font-weight: bold;
    font-family: helvetica;
    border-radius: inherit;
    position: relative;
    z-index: 1;
}

[data-progress]:after {
    content: '';
    background: rgb(218, 41, 28);
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    height: 60px;
    transform-origin: top center;
    z-index: 0;
    border-radius: 0 0 180px 180px;
    box-shadow: 0 0 5px rgb(218, 41, 28);
}

[data-progress="50"]:after {
    transform: rotate(90deg);
}

.ogm-test .interaction-table-mood {
    display: flex;
    justify-content: flex-end;
}

.ogm-test .interaction-table-mood a {
    background-color: #fff;
    color: rgb(218, 41, 28);
    border: 1px solid rgb(218, 41, 28);
    padding: 0.35rem 1.35rem;
    border-radius: 10px;
}

.ogm-test .ogm-test-question-content {
    margin-top: 1.85rem;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

.ogm-test .ogm-test-question-content .question-content-head {
    padding: 1.75rem 0.5rem;
    background-color: rgb(218, 41, 28);
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
}


.ogm-test .ogm-test-question-content .question-content-head .question-content-head-text h2 {
    text-transform: uppercase;
    font-weight: 600;
    font-size: 25px;
    margin-bottom: 0;
    color: #fff;
    line-height: 2.5rem;
}

.ogm-test .ogm-test-question-content .question-content-head .question-content-head-text h2 span {
    background-color: #fff;
    color: rgb(218, 41, 28);
    border-radius: 10px;
    padding: 0.25rem 1rem;
}
.ogm-test .ogm-test-question-content .question-content-area-genel{
    border-right: 1px solid rgb(218, 41, 28);
    border-left: 1px solid rgb(218, 41, 28);
    border-bottom: 1px solid rgb(218, 41, 28);
    border-bottom-left-radius: 16px;
    border-bottom-right-radius: 16px;
    padding: 2rem 1rem;
}

.ogm-test .ogm-test-question-content .question-item {
    margin-bottom: 20px;
    padding: 15px 20px;
    page-break-inside: avoid;
    page-break-after: auto;
}

.question-content-details {
    position: relative;
}

.ogm-test-question-content .answer-info-test {
    border: 1px solid rgb(207, 207, 207);
    border-radius: 15px;
    padding: 0.95rem 1.15rem;
}

.ogm-test-question-content .answer-info-test .answer-text {
    margin-bottom: 0.5rem;
}

.ogm-test-question-content .answer-info-test .answer-text:last-child {
    margin-bottom: 0;
}

.ogm-test-question-content .answer-info-test .true-answer-text {
    color: darkgreen;
}

.ogm-test-question-content .answer-info-test .false-answer-text {
    color: maroon;
}

.ogm-test-question-content .answer-info-test .null-answer-text {
    color: chocolate;
}

.ogm-test-question-content .question-content-break .cizgi {
    background-color: rgb(218, 41, 28);
    position: absolute;
    left: 50%;
    height: 38%;
    width: 1.35px;
}

.question-content-details .question-content-break .cizgi.cizgiUst {
    top: 40px;
}

.question-content-details .question-content-break .cizgi.cizgiAlt {
    bottom: 40px;
}

.question-content-details .question-content-break .image-ust {
    position: absolute;
    top: 47.5%;
    left: 43%;
    transform: rotate(90deg);
}

.question-content-details .question-content-break .image-ust img {
    width: 180px;
}


.ogm-test .ogm-test-question-content .question-number {
    color: rgb(56, 56, 56);
    font-size: 15px;
    font-weight: 600;
}

.ogm-test .ogm-test-question-content .form-check {
    margin-bottom: 10px;
    font-size: 14px;
}

.ogm-test .form-check-input {
    cursor: pointer;
}

.ogm-test .form-check-input:checked[type=radio] {
    background-image: none !important;
}

.ogm-test .form-check-input:checked {
    background-color: rgb(218, 41, 28);
    border-color: rgb(218, 41, 28);
}

.ogm-test .question-item .question-item-ask {
    font-size: 16px;
}

.ogm-test .ogm-test-question-content .question-content-foot {
    padding: 1.15rem 1.5rem;
    background-color: rgb(218, 41, 28);
    border-radius: 16px;
    margin-top: 1.5rem;
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .btn {
    border-radius: 12px;
    padding: 0.4rem 1.8rem;
    letter-spacing: -1px;
    font-size: 17px;
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .back-button .btn {
    background-color: #fff;
    border: 1px solid #fff;
    color: rgb(218, 41, 28);
}
.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .back-button .btn:hover{
    background-color: #f5f5f5;
    border: 1px solid #f5f5f5;
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .document-buttons a {
    color: #fff;
    font-size: 30px;
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .action-button .btn {
    background-color: #fff;
    border: 1px solid #fff;
    color: rgb(218, 41, 28);
}

.ogm-test .ogm-test-question-content .question-content-foot .question-content-foot-buttons .action-button .btn:hover{
    background-color: #f5f5f5;
    border: 1px solid #f5f5f5;
}



.baglamliTest .row {
    --bs-gutter-x: 2rem;
}

.baglamliTest .ask-action-button {
    margin-top: 1rem;
}

.baglamliTest .ask-action-button .btn {
    background-color: rgb(218, 41, 28);
    color: rgb(255, 255, 255);
    border-radius: 8px;
    font-size: 15px;
}

.baglamliTest .ask-action-button .cevap span {
    font-weight: bold;
    color: green;
}

.baglamliTest .baglamliTest-Head {
    background-color: #fcf0f0;
    border: 2px solid #fff;
    border-radius: 10px;
    padding: 0.95rem 1.65rem;
    color: #23272b;
    font-size: 15px;
    opacity: 0.8;
    margin-bottom: 1rem;
    letter-spacing: -1px;
    font-weight: 500;
}

.baglamliTest .answer-pagination-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 2px solid rgb(219, 219, 219);
    border-radius: 8px;
    padding: 1.15rem 1.05rem;
    margin-bottom: 1.5rem;
}

.baglamliTest .answer-pagination-buttons .nav-pills .nav-item {
    margin-right: 0.6rem;
}

.baglamliTest .answer-pagination-buttons .nav-pills .nav-link {
    background: rgb(211, 211, 211);
    color: #fff;
    font-size: 17px;
}

.baglamliTest .answer-pagination-buttons .nav-pills .nav-link.active {
    background: rgb(218, 41, 28);
}

.baglamliTest .answer-pagination-buttons .answer-navigation {
    display: flex;
    align-items: center;
}

.baglamliTest .answer-pagination-buttons .answer-navigation a {
    background-color: rgb(211, 211, 211);
    color: #fff;
    padding: 0 0.5rem;
    border: 1px solid rgb(211, 211, 211);
    border-radius: 4px;
    font-size: 25px;
}

.baglamliTest .answer-pagination-buttons .answer-navigation a:hover {
    background-color: rgb(218, 41, 28);
}

.baglamliTest .accordion-button::after {
    width: 1rem;
    height: 1rem;
    background-size: 1rem;
}

.baglamliTest .accordion-button:not(.collapsed) {
    color: #fff;
    background-color: rgb(218, 41, 28);
}

.baglamliTest .accordion-button:not(.collapsed)::after {
    background-image: url('https://ogmmateryal.eba.gov.tr/assets/img/light-arrow.svg')
}

.baglamliTest .accordion-item {
    border-bottom: 1px solid rgb(138 138 138 / 13%);
}

.baglamliTest .accordion-flush .accordion-item .accordion-button {
    border-radius: 6px;
}

.baglamliTest .accordion-item .accordion-body {
    font-size: 15px;
}

.baglamliTest .baglamliHead {
    font-weight: 600;
    font-size: 17px;
    position: relative;
    margin-bottom: 2rem;
}

.baglamliTest .baglamliHead::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    background-color: rgb(218, 41, 28);
    width: 50px;
    height: 1.5px;
}

.baglamliTest .baglamli-soruAlani {
    border-right: 1px solid #bebebe;
}

.baglamliTest .baglamli-soruAlani .question-head {
    font-weight: 600;
    font-size: 17px;
    margin-bottom: 0.55rem;
}


.action-board .page-item.active .page-link {
    background-color: rgb(218, 41, 28);
    border-color: rgb(218, 41, 28);
}

.action-board .page-link {
    color: rgb(218, 41, 28);
}

.action-board .pagination {
    margin-bottom: 0;
}

.get-Question {
    display: flex;
    align-items: center;
}

.get-Question .question-number-form {
    margin-right: 0.95rem;
}

.get-Question .question-number-form .form-control {
    border-radius: 6px;
}

.get-Question .question-number-form .form-control:focus {
    box-shadow: none;
    border-color: rgb(218, 41, 28);
}

.get-Question .question-number-button .btn {
    background-color: #23272b;
    color: #fff;
    padding: 0.35rem 1.05rem;
    border-radius: 6px;
}

.get-Question .question-number-button .btn:focus {
    box-shadow: none;
}

.action-board-section .action-board-question-box {
    width: 50%;
}

.action-board-section .action-board-question-box .question-answer .form-check {
    margin-bottom: 0.35rem;
    padding-left: 0;
}

.action-board-section .action-board-question-box .question-answer .form-check:last-child {
    margin-bottom: 0;
}



.quantity .input-text.qty {
    width: 35px;
    height: 39px;
    padding: 0 5px;
    text-align: center;
    background-color: transparent;
    border: 1px solid #efefef;
}

.quantity.buttons_added {
    display: flex;
    align-items: center;
}

.quantity.buttons_added input {
    display: inline-block;
    margin: 0;
    vertical-align: top;
    box-shadow: none;
    height: 40px !important;
}

.quantity.buttons_added .minus,
.quantity.buttons_added .plus {
    padding: 7px 10px 8px;
    background-color: #f5f5f5;
    border: 1px solid #ebebeb;
    cursor: pointer;
}

.quantity.buttons_added .minus {
    border-right: 0;
}

.quantity.buttons_added .plus {
    border-left: 0;
    color: rgb(218, 41, 28);
}

.quantity.buttons_added .minus:hover,
.quantity.buttons_added .plus:hover {
    background: #eeeeee;
}

.quantity input::-webkit-outer-spin-button,
.quantity input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    -moz-appearance: none;
    margin: 0;
}

.quantity.buttons_added .minus:focus,
.quantity.buttons_added .plus:focus {
    outline: none;
}


.books-detail .row {
    --bs-gutter-x: 2.85rem;
}

.books-detail-2 .row {
    --bs-gutter-x: 3.45rem;
}

.books-detail .books-detail-box {
    padding: 1rem;
    box-shadow: rgb(99 99 99 / 20%) 0px 1px 8px 1px;
    text-align: center;
    vertical-align: middle;
    height: 220px;
    position: relative;
    border-radius: 30px;
    transition: all .1s ease;
    background-color: #e9ecef;
}

.books-detail .books-detail-box:hover {
    box-shadow: rgb(218 41 28 / 50%) 0px 1px 8px 1px;
}

    .books-detail .books-detail-box .books-detail-content {
        position: absolute;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        width: 100%;
        height: 100%;
        
    }

.books-detail .books-detail-box .books-detail-content a {
    display: block;
    width: 100%;
    height: 100%;
    color: #000;
    position: absolute;
    padding: 3.15rem 2rem 3.5rem 2rem;
}

.books-detail .books-detail-box .books-detail-content .books-detail-icon {
    font-size: 38px;
    color: rgb(218, 41, 28);
    margin-bottom: 0.65rem;
}

    .books-detail .books-detail-box .books-detail-content .books-detail-icon img{
        max-width:100px;
    }

    .books-detail .books-detail-box .books-detail-content .books-detail-head h4 {
        
        letter-spacing: -1px;
        font-size: 22px;
    }


.books-detail-action .books-detail-action-head {
    margin-bottom: 1.5rem;
}

.books-detail-action .books-detail-action-head h4 {
    font-size: 18px;
    position: relative;
    margin-bottom: 0;
}

.books-detail-action .books-detail-action-head h4::after {
    content: "";
    position: absolute;
    bottom: -7px;
    left: 0;
    background: rgb(218, 41, 28);
    width: 30px;
    height: 2px;
}

.books-detail-action .row {
    --bs-gutter-x: 2.85rem;
}

.books-detail-action-content {
    position: relative;
    border-radius: 6px;
}

.books-detail-action-content img {
    
}

.books-detail-action-buttons {
    position: absolute;
    left: 0;
    bottom: 0;
    right: 0;
    height: 40px;
    transition: ease-in-out 0.2s;
    background: #f6f6f6;
    opacity: 0.9;
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.books-detail-action-buttons a {
    transition: color 0.1s;
    color: #23272b;
    font-size: 18px;
    margin-right: 17px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.books-detail-action-buttons a:hover {
    color: rgb(218, 41, 28);
}

.books-detail-action-buttons a:last-child {
    margin-right: 0;
}


.ogm-yks .ogm-yks-head {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 1.85rem;
    position: relative;
}

.ogm-yks .ogm-yks-head::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    background: rgb(218, 41, 28);
    width: 45px;
    height: 2px;
}

.ogm-yks .ogm-yks-item {
    padding: 2.5rem 0;
    border-bottom: 1px solid rgb(189, 189, 189);
}

.ogm-yks .ogm-yks-item:last-child {
    border-bottom: 0 !important;
    padding-bottom: 1rem !important;
}

.ogm-yks .ogm-yks-item .yks-item-head {
    margin-bottom: 1.2rem;
}

.ogm-yks .ogm-yks-item .yks-item-head h5 {
    font-size: 19px;
    font-weight: 600;
    margin-bottom: 1.85rem;
    position: relative;
}

.ogm-yks .ogm-yks-item .yks-item-head h5::after {
    content: "";
    position: absolute;
    bottom: -7px;
    left: 0;
    background: rgb(218, 41, 28);
    width: 35px;
    height: 2px;
}

.ogm-yks .ogm-yks-item .yks-item-content .row {
    --bs-gutter-x: 2.55rem;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-img {
    position: relative;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-img img {
    width: 100%;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-img img:hover {
    opacity: 0.9;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-img .content-img-number {
    position: absolute;
    bottom: 13px;
    left: 47.5%;
    font-size: 24px;
    font-weight: 600;
    font-family: 'Roboto Mono', monospace !important;
    color: #fff;
}


.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-buttons {
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgb(219, 219, 219);
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
    padding: 0.2rem 0;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-buttons .button-pdf {
    margin-right: 0.8rem;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-buttons .button-pdf a {
    color: #23272b;
    font-size: 27px;
}

.ogm-yks .ogm-yks-item .yks-item-content .yks-item-content-buttons .button-youtube a {
    color: rgb(218, 41, 28);
    font-size: 31px;
}

.ogm-yks .swiper-button-next,
.ogm-yks .swiper-button-prev {
    background-color: #fff;
    color: #23272b;
    padding: 1.35rem 1.25rem;
}

.ogm-yks .swiper-button-next {
    right: 0;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    padding-right: 0.95rem;
}

.ogm-yks .swiper-button-prev {
    left: 0;
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
    padding-left: 0.95rem;
}

.ogm-yks .swiper-button-next::after,
.ogm-yks .swiper-button-prev::after {
    font-size: 25px;
}


.ogm-yks-training .row {
    --bs-gutter-x: 2.5rem;
}

.ogm-yks-training .yks-training-sidebar .sidebar-select-list {
    margin-bottom: 0.9rem;
}

.ogm-yks-training .yks-training-sidebar .sidebar-select-list .form-select {
    border-radius: 12px;
    font-size: 15px;
    letter-spacing: -1px;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.65rem;
    border-bottom: 1px solid rgb(218, 218, 218);
    padding: 0.65rem 0;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item:first-child {
    padding-top: 0;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item:last-child {
    border-bottom: 0;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-head {
    display: flex;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-head .head-category {
    margin-right: 1rem;
    font-size: 15px;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-head .head-text {
    font-size: 15px;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-head .head-text a {
    color: rgb(33, 37, 41);
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-action {
    display: flex;
    align-items: center;
}

.ogm-yks-training .yks-training-sidebar .sidebar-content-item .content-item-action a {
    color: rgb(218, 41, 28);
    font-size: 18px;
    margin-right: 0.5rem;
}

.ogm-yks-training .yks-training-content .pdf-content,
.ogm-yks-training .yks-training-content .video-content {
    
    width: 100%;
    overflow: auto;
}


.ogm-models .row {
    --bs-gutter-x: 3rem;
}

.ogm-models .models-item {
    border-radius: 15px;
    border: 1px solid rgb(172, 172, 172);
}

.ogm-models .models-item .model-img {
    position: relative;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.ogm-models .models-item .model-img img {
    width: 100%;
    height: 270px;
    object-fit: cover;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
}

.ogm-models .models-item .model-img .model-class-info {
    position: absolute;
    top: 10px;
    right: 10px;
}

.ogm-models .models-item .model-img .model-class-info span {
    background: rgb(218, 41, 28);
    color: #fff;
    padding: 0.35rem 0.55rem;
    border-radius: 6px;
    font-size: 13px;
}

.ogm-models .models-item .model-content {
    padding: 1rem;
    border-top: 1px solid rgb(172, 172, 172);
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    min-height: 130px;
}

.ogm-models .models-item .model-content .model-head {
    border-bottom: 1px solid rgb(180, 180, 180);
}

.ogm-models .models-item .model-content .model-head a {
    color: #23272b;
}

.ogm-models .models-item .model-content .model-head h5 {
    font-weight: 600;
    font-size: 17px;
}

.ogm-models .models-item .model-content .model-text {
    font-size: 14px;
    font-weight: 400;
    line-height: 1.15rem;
}

.ogm-models .models-item .model-content .download-icon a {
    color: rgb(218, 41, 28);
}


.ogm-felsefe-sozluk .sozlukContent {
    display: flex;
    border: 2px solid rgb(218, 41, 28);
    padding: 2rem;
    border-radius: 20px;
}

.ogm-felsefe-sozluk .nav-pills .nav-link.active,
.ogm-felsefe-sozluk .nav-pills .show>.nav-link {
    background-color: rgb(218, 41, 28);
    color: #fff;
    border: 1px solid rgb(218, 41, 28);
}

.ogm-felsefe-sozluk .nav-link {
    color: rgb(218, 41, 28);
    border: 1px solid rgb(216, 216, 216);
    margin-bottom: 0.85rem;
    padding: 0.25rem 0.65rem;
}

.ogm-felsefe-sozluk .nav-link:last-child {
    margin-bottom: 0;
}

.ogm-felsefe-sozluk .sozlukList {
    margin-bottom: 0;
}

.ogm-felsefe-sozluk .sozlukList li {
    margin-bottom: 0.65rem;
    padding-bottom: 0.65rem;
    border-bottom: 1px solid rgb(224, 224, 224);
}

.ogm-felsefe-sozluk .sozlukList li:last-child {
    border-bottom: 0;
    margin-bottom: 0;
    padding-bottom: 0;
}

.ogm-felsefe-sozluk .sozlukList li a {
    color: #23272b;
    font-size: 14px;
}

.ogm-felsefe-sozluk .sozlukList li a.active {
    font-weight: 600;
}

.ogm-felsefe-sozluk .video-content .video-head {
    margin-bottom: 0.85rem;
    text-align: center;
}

.ogm-felsefe-sozluk .video-content .video-head h3 {
    font-size: 18px;
    border-bottom: 1px solid rgb(218, 41, 28);
    padding-bottom: 0.25rem;
    display: inline-block;
}


.ogm-sairler tbody,
.ogm-sairler td,
.ogm-sairler tfoot,
.ogm-sairler th,
.ogm-sairler thead,
.ogm-sairler tr {
    font-size: 14px;
}

.ogm-sairler .table .table-action {
    font-size: 18px;
    color: rgb(218, 41, 28);
}

.ogm-sairler .video-content {
    background-color: #484d52;
    color: #fff;
    padding: 1.5rem;
    border-radius: 5px;
    position: sticky;
    top: 108px;
}

.ogm-sairler .video-content .video-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.85rem;
}

.ogm-sairler .video-content .video-head h3 {
    font-size: 15px;
    margin-bottom: 0;
    font-weight: 500;
}

.ogm-sairler .video-content .video-head h3 span {
    font-weight: 600;
}

.ogm-sairler .video-content .video-head .sair-info {
    font-size: 15px;
}


.word-mean .row{
    --bs-gutter-x: 3rem;
}
.word-mean .mean-item{
    border-bottom: 1px solid rgb(236, 236, 236);
    padding-bottom: 0.35rem;
    text-align: center;
}
.word-mean .mean-item a{
    color: #23272b;
    font-size: 15px;
}
#kelimeModal .modal-title{
    margin-bottom: 0;
    font-weight: 600;
    font-size: 17px;
}
#kelimeModal .modal-body{
    font-weight: 400;
    font-size: 15px;
    padding: 1.5rem 1rem;
}
#kelimeModal button:focus{
    box-shadow: none;
}


.ogm-atasozleri-deyimler .atasozleri-deyimler-head{
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid rgb(224, 224, 224);
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item{
    width: 2.25%;
    margin-right: 0.85rem;
    position: relative;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item::after{
    content: "";
    position: absolute;
    top: 50%;
    left: 72%;
    width: 12px;
    height: 2px;
    background-color: rgb(218, 41, 28);
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item.son-item::after{
    content: none;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item:last-child{
    margin-right: 0;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item a{
    color: #23272b;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-head .head-item a.active{
    font-weight: 600;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-content{
    margin-top: 1rem;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-content ul{
    list-style: square;
    padding-left: 1rem;
    margin-bottom: 0;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-content ul li{
    margin-bottom: 0.5rem;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-content ul li:last-child{
    margin-bottom: 0;
}
.ogm-atasozleri-deyimler .atasozleri-deyimler-content ul li a{
    color: #23272b;
    font-size: 15px;
    cursor: pointer;
}
#atasozuModal .modal-title, #deyimlerModal .modal-title{
    margin-bottom: 0;
    font-weight: 600;
    font-size: 17px;
}
#atasozuModal .modal-body, #deyimlerModal .modal-body{
    font-weight: 400;
    font-size: 15px;
    padding: 1.5rem 1rem;
}
#atasozuModal button:focus, #deyimlerModal button:focus{
    box-shadow: none;
}



#ogm-foot {
    background-color: #23272b;
    padding: 1.5rem 0;
}

#ogm-foot .ogm-foot-items {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgb(82, 82, 82);
    padding-bottom: 1rem;
}

#ogm-foot .ogm-foot-items .ogm-foot-social {
    list-style: none;
    margin-bottom: 0;
    padding-left: 0;
    display: flex;
    align-items: center;
}

#ogm-foot .ogm-foot-items .ogm-foot-social li {
    margin-right: 1.05rem;
}

#ogm-foot .ogm-foot-items .ogm-foot-social li:last-child {
    margin-right: 0;
}

#ogm-foot .ogm-foot-items .ogm-foot-social li a {
    color: #fff;
    font-size: 20px;
}


.ogm-sss .row {
    --bs-gutter-x: 3.15rem;
}

.ogm-sss .sss-list {
    list-style-type: square;
    padding-left: 1rem;
    margin-bottom: 0;
}

.ogm-sss .sss-list li {
    margin-bottom: 0.65rem;
}

.ogm-sss .sss-list li:last-child {
    margin-bottom: 0;
}

.ogm-sss .sss-list li a {
    color: #000;
    font-weight: 500;
    font-size: 15px;
}

.ogm-sss .sss-list li a.active-question {
    font-weight: 600;
}

.ogm-sss .sss-item-1 {
    border-right: 1px solid rgb(228, 228, 228);
}

.ogm-sss .video-area {
    background-color: #23272b;
    padding: 1rem 1.35rem;
    border-radius: 7px;
}

.ogm-sss .video-area .video-head {
    color: #fff;
    text-align: center;
    margin-bottom: 0.75rem;
}

.ogm-sss .video-area .video-head h4 {
    font-size: 17px;
}


#ogm-foot .foot-app-images {
    display: flex;
    justify-content: flex-end;
    align-items: center;

}

#ogm-foot .foot-app-images .app-img-item {
    margin-right: 1rem;
}

#ogm-foot .foot-app-images .app-img-item:last-child {
    margin-right: 0;
}

#ogm-foot .foot-app-images .app-img-item img {
    width: 100px;
}


#ogm-foot .foot-menu-items {
    border-bottom: 1px solid rgb(82, 82, 82);
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}

#ogm-foot .foot-menu-items .foot-menu-logo-item img {
    width: 210px;
}

#ogm-foot .foot-menu-items .foot-menu-head {
    margin-bottom: 1.8rem;
}

#ogm-foot .foot-menu-items .foot-menu-head h3 {
    color: #fff;
    font-weight: 600;
    font-size: 18px;
    position: relative;
}

#ogm-foot .foot-menu-items .foot-menu-head h3::after {
    display: block;
    height: 2px;
    margin-top: 0;
    margin-bottom: -13px;
    content: '';
    position: absolute;
    bottom: 0;
    background-color: #fff;
    width: 30px;
}

#ogm-foot .foot-menu-items .foot-menu-links {
    list-style: none;
    padding-left: 0;
    margin-bottom: 0;
}

#ogm-foot .foot-menu-items .foot-menu-links li {
    margin-bottom: 0.35rem;
    color: #fff;
    font-size: 14px;
}

#ogm-foot .foot-menu-items .foot-menu-links li a {
    font-size: 14px;
    font-weight: 400;
    color: #fff;
}

#ogm-foot .foot-menu-items .foot-menu-links li a:hover {
    color: rgb(218, 41, 28);
}


.foot-copyright {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 1.15rem;
}

.foot-copyright .copyright-item span {
    font-size: 14px;
    color: #fff;
}</style><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="/assets/css/responsive.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <link rel="stylesheet" href="/assets/css/swiper-bundle.min.css"><style class="darkreader darkreader--sync" media="screen"></style>
    <script src="/assets/js/swiper-bundle.min.js"></script><meta name="darkreader" content="816de8fbf8684dfe9d1bca1c11985b52"><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: var(--darkreader-background-ffd76e, #684b00) !important;
    border-color: var(--darkreader-background-c59d00, #9e7e00) !important;
    color: var(--darkreader-text-302505, #d7d4cf) !important;
}
#vimvixen-console-frame {
    color-scheme: light !important;
}
::placeholder {
    opacity: 0.5 !important;
}
#edge-translate-panel-body,
.MuiTypography-body1,
.nfe-quote-text {
    color: var(--darkreader-neutral-text) !important;
}
gr-main-header {
    background-color: var(--darkreader-background-add8e6, #1b4958) !important;
}
.tou-z65h9k,
.tou-mignzq,
.tou-1b6i2ox,
.tou-lnqlqk {
    background-color: var(--darkreader-neutral-background) !important;
}
.tou-75mvi {
    background-color: var(--darkreader-background-cfecf5, #0f3a47) !important;
}
.tou-ta9e87,
.tou-1w3fhi0,
.tou-1b8t2us,
.tou-py7lfi,
.tou-1lpmd9d,
.tou-1frrtv8,
.tou-17ezmgn {
    background-color: var(--darkreader-background-f5f5f5, #1e2021) !important;
}
.tou-uknfeu {
    background-color: var(--darkreader-background-faedda, #432c09) !important;
}
.tou-6i3zyv {
    background-color: var(--darkreader-background-85c3d8, #245d70) !important;
}
div.mermaid-viewer-control-panel .btn {
    background-color: var(--darkreader-neutral-background);
    fill: var(--darkreader-neutral-text);
}
svg g rect.er {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.entityBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxOdd {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.er.attributeBoxEven {
    fill: var(--darkreader-selection-background);
    fill-opacity: 0.8 !important;
}
svg rect.er.relationshipLabelBox {
    fill: var(--darkreader-neutral-background) !important;
}
svg g g.nodes rect,
svg g g.nodes polygon {
    fill: var(--darkreader-neutral-background) !important;
}
svg g rect.task {
    fill: var(--darkreader-selection-background) !important;
}
svg line.messageLine0,
svg line.messageLine1 {
    stroke: var(--darkreader-neutral-text) !important;
}
div.mermaid .actor {
    fill: var(--darkreader-neutral-background) !important;
}
mitid-authenticators-code-app > .code-app-container {
    background-color: white !important;
    padding-top: 1rem;
}
iframe#unpaywall[src$="unpaywall.html"] {
    color-scheme: light !important;
}
select option {
    background-color: var(--darkreader-neutral-background) !important;
}
body#tumblr {
    --darkreader-bg--secondary-accent: 31, 32, 34 !important;
    --darkreader-bg--white: 23, 23, 23 !important;
    --darkreader-text--black: 228, 224, 218 !important;
}
:host {
    --d2l-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-button-icon-background-color-hover: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-color-ferrite: var(--darkreader-neutral-text) !important;
    --d2l-color-sylvite: var(--darkreader-bg--d2l-color-sylvite) !important;
    --d2l-dropdown-background-color: var(--darkreader-neutral-background) !important;
    --d2l-dropdown-border-color: var(--darkreader-border--d2l-color-mica) !important;
    --d2l-input-backgroud-color: var(--darkreader-neutral-background) !important;
    --d2l-menu-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
    --d2l-tooltip-background-color: var(--darkreader-neutral-background) !important;
    --d2l-tooltip-border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
:host([_floating]) .d2l-floating-buttons-container {
    background-color: var(--darkreader-neutral-background) !important;
    border-top-color: var(--darkreader-border--d2l-color-mica) !important;
    opacity: 0.88 !important;
}
d2l-card {
    background: var(--darkreader-neutral-background) !important;
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
d2l-dropdown-content > div,
d2l-menu-item {
    background-color: var(--darkreader-neutral-background) !important;
    border-radius: 10px !important;
}
d2l-empty-state-simple {
    border-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-button-filter > ul > li > a.vui-button {
    border-color: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-label-text:has(.d2l-button-subtle-content):hover,
.d2l-label-text:has(.d2l-button-subtle-content):focus,
.d2l-label-text:has(.d2l-button-subtle-content):active {
    background-color: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-navigation-centerer {
    color: inherit !important;
}
.d2l-tabs-layout {
    border-color: var(--darkreader-border--d2l-color-gypsum) !important;
}
.d2l-input,
.d2l-calendar-date,
.d2l-htmleditor-container {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-collapsible-panel {
    border: 1px solid var(--darkreader-border--d2l-color-mica) !important;
    border-radius: 0.4rem !important;
}
.d2l-collapsible-panel-divider {
    border-bottom: 1px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-w2d-flex {
    border-bottom: 2px solid var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-collapsible-panel scrolled,
.d2l-collapsible-panel-header,
.d2l-w2d-collection-fixed {
    background-color: var(--darkreader-neutral-background) !important;
}
.d2l-loading-spinner-bg {
    fill: var(--darkreader-bg--d2l-color-gypsum) !important;
}
.d2l-loading-spinner-bg-stroke {
    stroke: var(--darkreader-border--d2l-color-mica) !important;
}
.d2l-loading-spinner-wrapper svg path,
.d2l-loading-spinner-wrapper svg circle {
    fill: var(--darkreader-neutral-background) !important;
}</style>
    <title>YKS Konu Anlatımları | OGM Materyal</title>
    <script type="text/javascript">
        if (location.protocol !== 'https:') {
            location.replace(`https:${location.href.substring(location.protocol.length)}`);
        }
    </script>
    <style type="text/css">
        .ogm-main-menu-bottom .select-box {
            width: 18%;
        }

        .ogm-main-menu-bottom .select-btn-box {
            width: 18%;
        }

            .ogm-main-menu-bottom .select-btn-box .btn {
                background-color: rgb(218, 41, 28);
                width: 100%;
                color: #fff;
                border-radius: 12px;
                letter-spacing: -1px;
            }

        @media(max-width:600px) {
            .ogm-main-menu-bottom .select-box {
                width: 48%;
            }

            .ogm-main-menu-bottom .select-btn-box {
                margin-top: 0.95rem;
                width: 100%;
            }
        }

        .books-detail-action-content {
            box-shadow: 1px 1px 5px 0px black;
        }


        .blink {
            -webkit-animation: 1s linear infinite condemned_blink_effect;
            animation: 1s linear infinite condemned_blink_effect;
            color: red;
        }

        @-webkit-keyframes condemned_blink_effect {
            0% {
                visibility: hidden;
            }

            50% {
                visibility: hidden;
            }

            100% {
                visibility: visible;
            }
        }

        @keyframes condemned_blink_effect {
            0% {
                visibility: hidden;
            }

            50% {
                visibility: hidden;
            }

            100% {
                visibility: visible;
            }
        }
    </style><style class="darkreader darkreader--sync" media="screen"></style>
    
    <style type="text/css">
        .ogm-main-menu-bottom .select-box {
            width: 80%;
        }

        @media(max-width:600px) {
            .ogm-main-menu-bottom .select-box {
                width: 100%;
            }

            .ogm-main-menu-bottom .select-btn-box {
                margin-top: 0.95rem;
                width: 100%;
            }
        }

        .secili, .secili a {
            color: rgb(218, 41, 28) !important;
        }
    </style><style class="darkreader darkreader--sync" media="screen"></style>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-114103913-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'UA-114103913-1');
    </script>
</head>
<body>
    <button id="scrollUp" title="Yukarı çık" style="display: none;"><svg class="svg-inline--fa fa-angle-up" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-up" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M352 352c-8.188 0-16.38-3.125-22.62-9.375L192 205.3l-137.4 137.4c-12.5 12.5-32.75 12.5-45.25 0s-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25C368.4 348.9 360.2 352 352 352z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-up"></i> Font Awesome fontawesome.com --></button>
    <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header d-block">
            <div class="offcanvas-head">
                <h5 id="offcanvasRightLabel">Menü</h5>
                <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Kapat"></button>
            </div>


        </div>
        <div class="offcanvas-body">
            <ul class="offcanvas-list">
                <li><a href="/">Anasayfa</a></li>
                <li><a href="/etkilesimli-kitaplar">Ders Kitapları</a></li>
                <li><a href="/etkilesimli-kitap/guzel-sanatlar-lisesi">Güzel Sanatlar Lisesi Kitapları</a></li>
                <li><a href="/etkilesimli-kitap/spor-lisesi">Spor Lisesi Kitapları</a></li>
                <li><a href="/beceri-temelli-kitaplar">Beceri Temelli Kitaplar</a></li>
                <li><a href="/soru-bankasi">Soru Bankası</a></li>
                <li><a href="/kazanim-kavrama-etkinlikleri">Kazanım Kavrama Etkinlikleri</a></li>
                <li><a href="/calisma-defterleri">Çalışma Defterleri</a></li>
                <li><a href="/YKSHazirlik">YKS Hazırlık</a></li>
                <li><a href="/ders-sunulari">Ders Anlatım Sunuları</a></li>
                <li><a href="/konu-ozetleri">Konu Özetleri</a></li>
                <li><a href="https://ogmmateryal.eba.gov.tr/ebatv-ogm/Default.aspx">Ders Anlatım Videoları</a></li>
                <li style="display:none;"><a href="/yaziliya-hazirlaniyorum">Yazılıya Hazırlanıyorum</a></li>
                <li><a href="/etkilesimli-uygulamalar">Etkileşimli Uygulamalar</a></li>
                <li><a href="/deneyler">Deneyler</a></li>
                <li><a href="/oyun-etkinlik">Oyun ve Etkinlik Kitapları</a></li>
                <li><a href="/kavram-ogretimi">Kavram Öğretimi Çalışmaları</a></li>
                <li><a href="/uc-boyutlu-modeller">3B Modeller</a></li>
                <li><a href="/dinamik-uygulamalar">Dinamik Uygulamalar</a></li>
                <li><a href="/projeler">Projeler</a></li>
                <li><a href="/liseye-hosgeldin">Liseye Hoş Geldin</a></li>
                <li><a href="/Defteri">Defterim</a></li>
                <li><a href="/kutuphane">Yönetici/Öğretmen Kütüphanesi</a></li>
            </ul>
        </div>
    </div>
    <div id="temp-menu"></div>
    <header id="ogm-head">
        <div class="ogm-top-menu">
            <div class="container-xl">
                <div class="d-flex justify-content-between align-items-center">
                    <ul class="ogm-head-social">
                        <li><a target="_blank" title="Youtube" href="https://www.youtube.com/c/Orta%C3%B6%C4%9FretimGenelM%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a></li>
                        <li><a target="_blank" title="X" href="https://twitter.com/meb_ogm"><svg class="svg-inline--fa fa-twitter" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="twitter" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M459.4 151.7c.325 4.548 .325 9.097 .325 13.65 0 138.7-105.6 298.6-298.6 298.6-59.45 0-114.7-17.22-161.1-47.11 8.447 .974 16.57 1.299 25.34 1.299 49.06 0 94.21-16.57 130.3-44.83-46.13-.975-84.79-31.19-98.11-72.77 6.498 .974 12.99 1.624 19.82 1.624 9.421 0 18.84-1.3 27.61-3.573-48.08-9.747-84.14-51.98-84.14-102.1v-1.299c13.97 7.797 30.21 12.67 47.43 13.32-28.26-18.84-46.78-51.01-46.78-87.39 0-19.49 5.197-37.36 14.29-52.95 51.65 63.67 129.3 105.3 216.4 109.8-1.624-7.797-2.599-15.92-2.599-24.04 0-57.83 46.78-104.9 104.9-104.9 30.21 0 57.5 12.67 76.67 33.14 23.72-4.548 46.46-13.32 66.6-25.34-7.798 24.37-24.37 44.83-46.13 57.83 21.12-2.273 41.58-8.122 60.43-16.24-14.29 20.79-32.16 39.31-52.63 54.25z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-twitter"></i> Font Awesome fontawesome.com --></a></li>
                        <li><a target="_blank" title="Instagram" href="https://www.instagram.com/meb_ogm/"><svg class="svg-inline--fa fa-instagram" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="instagram" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-instagram"></i> Font Awesome fontawesome.com --></a></li>
                    </ul>
                    <div class="mobil-app-icon">
                        <div class="mobil-app-icon-text">
                            <span>Mobil Uygulamalar:</span>
                        </div>
                        <div class="mobil-app-icon-item">
                            <a href="https://apps.apple.com/us/developer/ortaogretim-genel-mudurlugu/id1550749142" title="Apple Store" target="_blank"><svg class="svg-inline--fa fa-apple" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="apple" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-apple"></i> Font Awesome fontawesome.com --></a>
                        </div>
                        <div class="mobil-app-icon-item">
                            <a href="https://play.google.com/store/apps/developer?id=OGM+Materyal" target="=_blank" title="Google Play"><svg class="svg-inline--fa fa-google-play" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="google-play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l256.6-256L47 0zm425.2 225.6l-58.9-34.1-65.7 64.5 65.7 64.5 60.1-34.1c18-14.3 18-46.5-1.2-60.8zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-google-play"></i> Font Awesome fontawesome.com --></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="ogm-main-menu" id="stickyHead">
            <div class="container-xl">
                <div class="main-menu-items">
                    <div class="main-logo">
                        <a href="/"><img src="/assets/img/ogm-logo.png" alt="OGM Materyal"></a>
                    </div>
                    <ul class="main-menu-link">
                        <li><a title="Anasayfa" href="/"><svg class="svg-inline--fa fa-house" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="house" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-home"></i> Font Awesome fontawesome.com --></a></li>
                        <li class="ana-menu">
                            <a href="#" class="dropdown-toggle">Etkileşimli Kitaplar</a>
                            <ul class="sub-menu">
                                <li><a href="/etkilesimli-kitaplar">Ders Kitapları</a></li>
                                <li><a href="/etkilesimli-kitap/guzel-sanatlar-lisesi">Güzel Sanatlar Lisesi Kitapları</a>
                                </li><li><a href="/etkilesimli-kitap/spor-lisesi">Spor Lisesi Kitapları</a>
                                </li><li><a href="/kazanim-kavrama-etkinlikleri">Kazanım Kavrama Etkinlikleri</a></li>
                                <li><a href="/calisma-defterleri">Çalışma Defterleri</a></li>
                                <li><a href="/kavram-ogretimi">Kavram Öğretimi Çalışmaları</a></li>
                                <li><a href="/oyun-etkinlik">Oyun ve Etkinlik Kitapları</a></li>
                                <li><a href="/liseye-hosgeldin">Liseye Hoş Geldin</a></li>
                                <li><a href="/defterim">Defterim</a></li>
                            </ul>
                        </li>
                        <li><a href="/beceri-temelli-kitaplar">Beceri Temelli Kitaplar</a></li>

                        <li><a href="/soru-bankasi">Soru Bankası</a></li>
                        <li class="ana-menu">
                            <a href="#" class="dropdown-toggle">YKS Hazırlık</a>
                            <ul class="sub-menu">
                                <li><a href="/yks-cikmis-soru-kitaplari">YKS Çıkmış Soru Kitapları <sup class="blink">Yeni</sup></a></li>
                                <li><a href="/mebi-konu-ozetleri">MEBİ Konu Özeti Kitapları <sup class="blink">Yeni</sup></a></li>
                                <li><a href="/yks-konu-pekistirme">Dört Dörtlük Konu Pekiştirme Testleri <sup class="blink">Güncellendi</sup></a></li>
                                <li><a href="/yks-uc-adim-deneme">3 Adım Deneme Sınavları <sup class="blink">Güncellendi</sup></a></li>
                                <li><a href="/yks-uc-adim">3 Adım Soru Bankası <sup class="blink">Güncellendi</sup></a></li>
                                <li><a href="/yks-kampi">YKS Kampı</a></li>
                                <li><a href="/yks-konu-anlatim">Konu Anlatımları (Video)</a></li>
                                <li><a href="/yks-deneme-sinavlari">Çevrim İçi Denemeler</a></li>
                                <li><a href="https://ogmmateryal.eba.gov.tr/kutuphane/rehberlik">Rehberlik</a></li>
                                <li><a href="/yks-puan-hesaplama">YKS Puan Hesaplama Motoru <sup class="blink">Yeni</sup></a> </li>
                                <li><a href="/yks-cikmis-soru-cozumleri">YKS Çıkmış Soru Çözümleri <sup class="blink">Yeni</sup></a></li>
                            </ul>
                        </li>
                        <li class="ana-menu">
                            <a href="#" class="dropdown-toggle">Ders Anlatım</a>
                            <ul class="sub-menu">
                                <li><a href="/konu-ozetleri">Konu Özetleri</a></li>
                                <li><a href="/ders-sunulari">Ders Anlatım Sunuları</a></li>
                                <li><a href="https://ogmmateryal.eba.gov.tr/ebatv-ogm/Default.aspx">Ders Anlatım Videoları</a></li>
                                <li class="d-none"><a href="/yaziliya-hazirlaniyorum">Yazılıya Hazırlanıyorum</a></li>
                            </ul>
                        </li>


                        <li class="ana-menu" style="display:none;">
                            <a href="#" class="dropdown-toggle">Uygulamalar</a>
                            <ul class="sub-menu">
                                <li><a href="/uc-boyutlu-modeller">3B Modeller</a></li>
                                <li><a href="/dinamik-uygulamalar">Dinamik Uygulamalar</a></li>
                                <li><a href="/etkilesimli-uygulamalar">Etkileşimli Uygulamalar</a></li>
                            </ul>
                        </li>
                        <li><a class="ana-menu btn" style="background-color: rgb(218, 41, 28); color: rgb(255, 255, 255); --darkreader-inline-bgcolor: var(--darkreader-background-da291c, #ae2116); --darkreader-inline-color: var(--darkreader-text-ffffff, #e8e6e3);" href="/kutuphane" data-darkreader-inline-bgcolor="" data-darkreader-inline-color="">Yönetici ve Öğretmen Kütüphanesi</a></li>
                        <li class="ana-menu" style="display:none;">
                            <a href="#" class="dropdown-toggle">Projeler</a>
                            <ul class="sub-menu">
                                <li><a href="/deneyler">Deneyler</a></li>
                                <li><a href="/felsefe-sozlugu">Canlı Felsefe Sözlüğü</a></li>
                                <li><a href="/sairlerin-dilinden">Şairlerin Dilinden</a></li>
                                <li><a href="/aktif-sozluk">Aktif Sözlük</a></li>
                                <li style="display:none;"><a href="/atasozleri">Söz Varlığımız: Atasözleri</a></li>
                                <li style="display:none;"><a href="/deyimler">Söz Varlığımız: Deyimler</a></li>
                                <li><a href="https://ogm.eba.gov.tr" target="_blank">Bilgi Yarışması</a></li>
                                <li><a href="/dusunuyorum">Düşünüyorum Etkinlikleri</a></li>
                                <li><a href="https://ods.eba.gov.tr" target="_blank">Kendini Değerlendir</a></li>
                            </ul>
                        </li>
                    </ul>
                    <div class="main-menu-bar" id="newbutton" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </div>
        </div>

        
    <div class="ogm-main-menu-bottom">
        <div class="container-xl">
            <div class="main-menu-bottom-items mobile-menu-bottom">
                <form class="d-flex justify-content-between flex-wrap">
                    <div class="select-box mb-md-0 mb-3">
                        <select id="dlDersKodu" class="form-select">
                            <option value="BIY">BİYOLOJİ</option>
                            <option value="COG">COĞRAFYA</option>
                            <option value="DIN">DİN KÜLTÜRÜ VE AHLAK BİLGİSİ</option>
                            <option value="FEL">FELSEFE</option>
                            <option value="FIZ">FİZİK</option>
                            <option value="KIM">KİMYA</option>
                            <option value="MAT">MATEMATİK</option>
                            <option value="TAR">TARİH</option>
                            <option value="TDE">TÜRK DİLİ VE EDEBİYATI</option>
                        </select>
                    </div>
                    <div class="select-btn-box">
                        <button id="btnFiltrele" type="button" class="btn">Listele</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    </header>
    <div style="min-height:600px;">
        


<nav style="display:none;" aria-label="breadcrumb" class="py-3 breadcrumb-area">
    <div class="container-xl">
        <ol class="breadcrumb mb-0">
            <li class="breadcrumb-item"><a class="ogm-links" href="/?s=0&amp;d=0&amp;u=0&amp;k=0">Anasayfa</a></li>
            <li class="breadcrumb-item"><a class="ogm-links" href="/Home/YKSHazirlik?s=0&amp;d=0&amp;u=0&amp;k=0">YKS Hazırlık</a></li>
            <li class="breadcrumb-item active" aria-current="page">YKS Konu Anlatım (Video)</li>
        </ol>
    </div>
</nav>


<section class="ogm-yks-training pt-4 pb-5">
    <div class="container-xl">
        <div class="section-title">
            <h2>YKS Konu Anlatım (Video)</h2>
        </div>
        <div class="row">
            <div class="col-md-4 training-item-1">
                <div class="yks-training-sidebar">
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            TYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/JsCNYpWIk5s', this); return false;">
                                                HÜCRE ZARINDAN MADDE GEÇİŞLERİ
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/xm0rleinimn.pdf" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/JsCNYpWIk5s', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            TYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/ktqBzaTHuKo', this); return false;">
                                                MONOHİBRİT– DİHİBRİT ÇAPRAZLAMA VE ÇOK ALLELLİK
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/vvigwvglk2k.pdf" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/ktqBzaTHuKo', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/1D0UN_cIHfE', this); return false;">
                                                DNA REPLİKASYON MEKANİZMASI
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/sk0lrkmmf1r.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/1D0UN_cIHfE', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/RwbhieZ73us', this); return false;">
                                                PROTEİN SENTEZİ MEKANİZMASI
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/3fzmvenroul.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/RwbhieZ73us', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/KzPfwbFji-k', this); return false;">
                                                FOTOSENTEZ
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/onnp4u4mknh.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/KzPfwbFji-k', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/tHfn8A4iEyk', this); return false;">
                                                HÜCRESEL SOLUNUM
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/fuqxrddcrhc.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/tHfn8A4iEyk', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/48s51xoAW2I', this); return false;">
                                                BİTKİLERDE MADDE TAŞINMASI
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/xjv3ccahn55.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/48s51xoAW2I', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                                <div class="sidebar-content-item">
                                    <div class="content-item-head">
                                        <div class="head-category">
                                            AYT
                                        </div>
                                        <div class="head-text">
                                            <a href="#" onclick="videoGoster('https://www.youtube.com/embed/kj-N9O10PgA', this); return false;">
                                                BİTKİLERDE ÜREME
                                            </a>
                                        </div>
                                    </div>
                                    <div class="content-item-action">
                                        <a href="http://ogmmateryal.eba.gov.tr/panel/upload/kitap/fy1opftst33.pdf
" target="_blank"><svg class="svg-inline--fa fa-file-pdf" aria-hidden="true" focusable="false" data-prefix="far" data-icon="file-pdf" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M365.3 93.38l-74.63-74.64C278.6 6.742 262.3 0 245.4 0H64C28.65 0 0 28.65 0 64l.0065 384c0 35.34 28.65 64 64 64H320c35.2 0 64-28.8 64-64V138.6C384 121.7 377.3 105.4 365.3 93.38zM336 448c0 8.836-7.164 16-16 16H64.02c-8.838 0-16-7.164-16-16L48 64.13c0-8.836 7.164-16 16-16h160L224 128c0 17.67 14.33 32 32 32h79.1V448zM202 286.1c.877-2.688 1.74-5.398 2.582-8.145c1.434-5.762 7.488-31.54 7.488-52.47C212.1 207 197.1 192 178.6 192C160.1 192 145.1 207 145.1 225.5c0 .2969 .1641 28.81 13.85 62.3c-7.035 19.36-15.57 38.8-25.41 57.93c-21.49 10.11-39.24 22.23-52.8 36.07c-6.234 6.438-9.367 14.74-9.367 24.72c0 18.45 15.01 33.46 33.46 33.46c10.8 0 20.98-5.227 27.22-13.98c7.322-10.28 18.38-26.9 30.47-48.95c15.8-6.352 33.88-11.72 53.88-16c13.55 9.578 28.9 17.29 45.71 22.95c4.527 1.551 9.402 2.348 14.43 2.348c20.26 0 36.13-16.19 36.13-36.86c0-20.33-16.54-36.87-36.87-36.87h-3.705c-2.727 .125-20.51 1.141-45.37 5.367C216.9 308.9 208.6 298.3 202 286.1zM110.2 410.4c-3.273 4.688-12.03 2.777-12.03-5.312c0-1.754 .6289-3.43 1.729-4.555c9.02-9.219 19.94-17.05 31.85-23.72C122.3 393.1 114.3 404.7 110.2 410.4zM178.6 218.8c3.693 0 6.703 3.008 6.703 6.703c0 15.21-4.109 34.84-5.746 42.1C172.1 245 171.9 227.2 171.9 225.5C171.9 221.8 174.9 218.8 178.6 218.8zM162.3 348.3c6.611-13.48 13.22-28.46 19.38-44.7c6.389 10.92 14.56 21.86 24.96 31.97C192.6 338.8 177.4 342.9 162.3 348.3zM272.4 339.5h3.352c5.539 0 10.05 4.5 10.05 10.79c0 5.129-4.176 9.32-9.32 9.32c-2.029 0-4.059-.3164-5.852-.9414c-12.33-4.137-23.11-9.32-32.54-15.19C258.3 340.3 272.1 339.5 272.4 339.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-file-pdf"></i> Font Awesome fontawesome.com --></a>
                                        <a class="ikon" href="#" onclick="videoGoster('https://www.youtube.com/embed/kj-N9O10PgA', this); return false;"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a>
                                    </div>
                                </div>
                </div>
            </div>
            <div class="col-md-8 training-item-2">
                <div class="yks-training-content">
                    <div id="video" class="video-content" style="overflow:hidden; height:600px;">

                    </div>
                </div>
            </div>
        </div>
    </div>
</section>




    </div>
    <div class="modal" id="modal-eba-tv-giris" tabindex="-1">
        <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">EBA TV Video İnceleme</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul class="list-group">
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-dogm/video/Authority.aspx">Din Öğretimi Genel Müdürlüğü</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-mtegm/video/Authority.aspx">Mesleki ve Teknik Eğitim Genel Müdürlüğü</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-ogm/video/Authority.aspx">Ortaöğretim Genel Müdürlüğü</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-orgm/video/Authority.aspx">Özel Eğitim ve Rehberlik Hizmetleri Genel Müdürlüğü</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-tegm/video/Authority.aspx">Temel Eğitim Genel Müdürlüğü</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-pictes/video/Authority.aspx">PİKTES</a></li>
                        <li class="list-group-item"><svg class="svg-inline--fa fa-angle-right" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512" data-fa-i2svg=""><path fill="currentColor" d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-angle-right"></i> Font Awesome fontawesome.com --> <a href="http://ogmmateryal.eba.gov.tr/ebatv-orgm-eris/video/Authority.aspx">Erişilebilirlik ÖERHGM</a></li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Kapat</button>
                </div>
            </div>
        </div>
    </div>

    <footer id="ogm-foot">
        <div class="container-xl">
            <div class="ogm-foot-items">

                <div class="foot-app-images">
                    <div class="app-img-item">
                        <a href="https://apps.apple.com/us/developer/ortaogretim-genel-mudurlugu/id1550749142" title="Apple Store" target="_blank"><img src="/assets/img/app-store.png" title="Soru Bankası - App Store" alt="OGM Materyal Soru Bankası"></a>
                    </div>
                    <div class="app-img-item">
                        <a href="https://play.google.com/store/apps/developer?id=OGM+Materyal" target="=_blank" title="Google Play"><img src="/assets/img/google-play.png" title="Soru Bankası - Google Play Store" alt="OGM Materyal Soru Bankası"></a>
                    </div>
                </div>
                <ul class="ogm-foot-social">
                    <li><a target="_blank" title="Youtube" href="https://www.youtube.com/c/Orta%C3%B6%C4%9FretimGenelM%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC"><svg class="svg-inline--fa fa-youtube" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" data-fa-i2svg=""><path fill="currentColor" d="M549.7 124.1c-6.281-23.65-24.79-42.28-48.28-48.6C458.8 64 288 64 288 64S117.2 64 74.63 75.49c-23.5 6.322-42 24.95-48.28 48.6-11.41 42.87-11.41 132.3-11.41 132.3s0 89.44 11.41 132.3c6.281 23.65 24.79 41.5 48.28 47.82C117.2 448 288 448 288 448s170.8 0 213.4-11.49c23.5-6.321 42-24.17 48.28-47.82 11.41-42.87 11.41-132.3 11.41-132.3s0-89.44-11.41-132.3zm-317.5 213.5V175.2l142.7 81.21-142.7 81.2z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-youtube"></i> Font Awesome fontawesome.com --></a></li>
                    <li><a target="_blank" title="X" href="https://twitter.com/meb_ogm"><svg class="svg-inline--fa fa-twitter" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="twitter" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M459.4 151.7c.325 4.548 .325 9.097 .325 13.65 0 138.7-105.6 298.6-298.6 298.6-59.45 0-114.7-17.22-161.1-47.11 8.447 .974 16.57 1.299 25.34 1.299 49.06 0 94.21-16.57 130.3-44.83-46.13-.975-84.79-31.19-98.11-72.77 6.498 .974 12.99 1.624 19.82 1.624 9.421 0 18.84-1.3 27.61-3.573-48.08-9.747-84.14-51.98-84.14-102.1v-1.299c13.97 7.797 30.21 12.67 47.43 13.32-28.26-18.84-46.78-51.01-46.78-87.39 0-19.49 5.197-37.36 14.29-52.95 51.65 63.67 129.3 105.3 216.4 109.8-1.624-7.797-2.599-15.92-2.599-24.04 0-57.83 46.78-104.9 104.9-104.9 30.21 0 57.5 12.67 76.67 33.14 23.72-4.548 46.46-13.32 66.6-25.34-7.798 24.37-24.37 44.83-46.13 57.83 21.12-2.273 41.58-8.122 60.43-16.24-14.29 20.79-32.16 39.31-52.63 54.25z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-twitter"></i> Font Awesome fontawesome.com --></a></li>
                    <li><a target="_blank" title="Instagram" href="https://www.instagram.com/meb_ogm/"><svg class="svg-inline--fa fa-instagram" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="instagram" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fab fa-instagram"></i> Font Awesome fontawesome.com --></a></li>
                </ul>
            </div>
            <div class="foot-menu-items">
                <div class="row">
                    <div class="col-lg-3 col-md-6 col-12 mb-lg-0 mb-md-3 mb-4">
                        <div class="foot-menu-logo-item">
                            <img src="/assets/img/ogm-eba.png" alt="">
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-lg-0 mb-md-3 mb-4">
                        <div class="foot-menu-head">
                            <h3>Modül İşlemleri</h3>
                        </div>
                        <ul class="foot-menu-links">
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/yonlen.php?git=3">E-İçerik Hazırlama</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/yonlen.php?git=7">Yabancı Dil Metin Alıştırmaları</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/yonlen.php?git=6">Soru Modülü</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/panel/video/Authority.aspx">Video İnceleme</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="#" data-bs-toggle="modal" data-bs-target="#modal-eba-tv-giris">EBA TV TRT Video İnceleme</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/komisyon">Komisyon İzleme Sistemi</a></li>

                        </ul>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-lg-0 mb-md-3 mb-4">
                        <div class="foot-menu-head">
                            <h3>Hızlı Linkler</h3>
                        </div>
                        <ul class="foot-menu-links">
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="/etkilesimli-kitaplar">Ders Kitapları</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="/soru-bankasi">Soru Bankası</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="/konu-ozetleri">Konu Özetleri</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="/etkilesimli-uygulamalar">Etkileşimli Uygulamalar</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogmmateryal.eba.gov.tr/ebatv-ogm/Default.aspx">Ders Anlatım Videoları</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="/ders-sunulari">Ders Anlatım Sunuları</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="https://ogm.meb.gov.tr/" target="_blank">Ortaöğretim Genel Müdürlüğü</a></li>
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;<a href="http://ogmiyiornekler.meb.gov.tr/" target="_blank">Eğitimde İyi Örnekler</a></li>

                        </ul>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12 mb-lg-0 mb-md-3 mb-4">
                        <div class="foot-menu-head">
                            <h3>İletişim Bilgileri</h3>
                        </div>
                        <ul class="foot-menu-links">
                            <li>
                                <svg class="svg-inline--fa fa-location-dot" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="location-dot" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M192 0C85.97 0 0 85.97 0 192c0 77.41 26.97 99.03 172.3 309.7c9.531 13.77 29.91 13.77 39.44 0C357 291 384 269.4 384 192C384 85.97 298 0 192 0zM192 271.1c-44.13 0-80-35.88-80-80S147.9 111.1 192 111.1s80 35.88 80 80S236.1 271.1 192 271.1z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-map-marker-alt"></i> Font Awesome fontawesome.com -->&nbsp;Atatürk Bulvarı No:98, Milli Eğitim Bakanlığı
                                Merkez Bina, Kat:5<br>
                                Kızılay / ÇANKAYA / ANKARA
                            </li>
                            <li><svg class="svg-inline--fa fa-square-phone" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="square-phone" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M384 32H64C28.65 32 0 60.65 0 96v320c0 35.35 28.65 64 64 64h320c35.35 0 64-28.65 64-64V96C448 60.65 419.3 32 384 32zM351.6 321.5l-11.62 50.39c-1.633 7.125-7.9 12.11-15.24 12.11c-126.1 0-228.7-102.6-228.7-228.8c0-7.328 4.984-13.59 12.11-15.22l50.38-11.63c7.344-1.703 14.88 2.109 17.93 9.062l23.27 54.28c2.719 6.391 .8828 13.83-4.492 18.22L168.3 232c16.99 34.61 45.14 62.75 79.77 79.75l22.02-26.91c4.344-5.391 11.85-7.25 18.24-4.484l54.24 23.25C349.5 306.6 353.3 314.2 351.6 321.5z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-phone-square"></i> Font Awesome fontawesome.com -->&nbsp;<a href="#">0 (312) 413 1576</a></li>
                            <li><svg class="svg-inline--fa fa-envelope" aria-hidden="true" focusable="false" data-prefix="far" data-icon="envelope" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M448 64H64C28.65 64 0 92.65 0 128v256c0 35.35 28.65 64 64 64h384c35.35 0 64-28.65 64-64V128C512 92.65 483.3 64 448 64zM64 112h384c8.822 0 16 7.178 16 16v22.16l-166.8 138.1c-23.19 19.28-59.34 19.27-82.47 .0156L48 150.2V128C48 119.2 55.18 112 64 112zM448 400H64c-8.822 0-16-7.178-16-16V212.7l136.1 113.4C204.3 342.8 229.8 352 256 352s51.75-9.188 71.97-25.98L464 212.7V384C464 392.8 456.8 400 448 400z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="far fa-envelope"></i> Font Awesome fontawesome.com -->&nbsp;<a href="#">ogmmateryalveicerik@meb.gov.tr</a></li>
                        </ul>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <ul class="foot-menu-links">
                            <li><svg class="svg-inline--fa fa-right-long" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="right-long" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M504.3 273.6l-112.1 104c-6.992 6.484-17.18 8.218-25.94 4.406c-8.758-3.812-14.42-12.45-14.42-21.1L351.9 288H32C14.33 288 .0002 273.7 .0002 255.1S14.33 224 32 224h319.9l0-72c0-9.547 5.66-18.19 14.42-22c8.754-3.809 18.95-2.075 25.94 4.41l112.1 104C514.6 247.9 514.6 264.1 504.3 273.6z" data-darkreader-inline-fill="" style="--darkreader-inline-fill: currentColor;"></path></svg><!-- <i class="fas fa-long-arrow-alt-right"></i> Font Awesome fontawesome.com -->&nbsp;  <a style="color: rgb(255, 255, 255); --darkreader-inline-color: var(--darkreader-text-ffffff, #e8e6e3);" href="/basvuru" data-darkreader-inline-color="">OGM Materyal Komisyon Görevlendirme Başvurusu</a></li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="foot-copyright">
                <div class="copyright-item me-lg-0 me-3">
                    <span>Copyright © 2025. Tüm Hakları Saklıdır.</span>
                </div>
                <div class="copyright-item">
                    <span>Ortaöğretim Genel Müdürlüğü Öğretim Materyalleri ve İçerik Geliştirme Daire Başkanlığı</span>
                </div>
            </div>
        </div>
    </footer>

    <script src="/content/js/jquery-3.6.0.min.js"></script>
    <script src="/assets/js/main.js"></script>
    <script src="/assets/js/font-awesome.all.min.js"></script>
    <script src="/assets/js/bootstrap.bundle.min.js"></script>
    <script type="text/javascript">
        var sinifId = 0;
        var dersId = 0;
        var uniteId = 0;
        var kazanimId = 0;
    </script>

    <script type="text/javascript">
        function linkGuncelle() {
            $('.ogm-links').each(function () {

                var h = $(this).attr('href');
                var pos = h.indexOf('?');
                if (pos > -1) {
                    h = h.substring(0, pos);
                }
                $(this).attr('href', h + '?s=' + sinifId + '&d=' + dersId + '&u=' + uniteId + '&k=' + kazanimId);
            })
        }
    </script>

    <script></script>

    
    <script type="text/javascript">
        var dersKodu = "0";
    </script>
                <script type="text/javascript">
             dersKodu = 'BIY';
                </script>
    <script type="text/javascript">
        $(function () {
            if (dersKodu != "0" && dersKodu != '') {
                $('#dlDersKodu').val(dersKodu);
            } 

            $('#btnFiltrele').on('click', function () {
                window.location.href = '/yks-konu-anlatim?kod=' + $('#dlDersKodu').val() + '&s=' + sinifId + '&d=' + dersId + '&u=' + uniteId + '&k=' + kazanimId;
            });
        })

        function videoGoster(file, el) {
            $('.sidebar-content-item').removeClass('secili');
            if ($(el).hasClass('ikon')) $(el).parent().parent().addClass('secili');
            else
                $(el).parent().parent().parent().addClass('secili');
            
            $('#video').html('<iframe style="height:100%;width:100%" frameborder="0" height="100%" width="100%" src = "' + file + '"></iframe >');
            $('html, body').animate({
                scrollTop: $('#video').offset().top - 200
            }, 200);
        }

        linkGuncelle();
    </script>


</body></html>
"""




from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from base_scraper import BaseScraper

html = BeautifulSoup(html, 'lxml')
scraper = BaseScraper()
items = html.select('.sidebar-content-item')
for item in items:
    sinav_tipi = item.select_one('.head-category').get_text() or ''
    sinav_tipi = scraper.clean_text(sinav_tipi)

    konu = item.select_one('.head-text').get_text() or ''
    konu = scraper.clean_text(konu)

    action_links = item.select('.content-item-action a')

    print(sinav_tipi)
    print(konu)
    print('------------------- links -------------------')
    for action_link in action_links:
        link = action_link.get('href')
        if '.pdf' in link:
            print("pdf LInks ",  link)

        else:
            onlick = action_link.get('onclick')
            print(onlick)

        print('-------------------')
    
    break

    