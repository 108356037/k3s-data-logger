{{- define "waterlogger.deployment.labels" }}
app: {{ .Values.appConfig.appName }}
stage: {{ .Values.environment }}
managed-by: {{ .Release.Service }}
date: {{ now | htmlDate }}
chart: {{ .Chart.Name }}
version: {{ .Chart.Version }}
{{- end }}

{{- define "waterlogger.deployment.selectorLabels" }}
app: {{ .Values.appConfig.appName }}
{{- end }}

{{- define "waterlogger.template.labels"}}
app: {{ .Values.appConfig.appName -}}
{{ end }}

{{- define "waterlogger.deployment.containerspec"}}
- image: {{ .Values.appConfig.appRepository }}/{{ .Values.appConfig.appImage }}:{{ .Values.appConfig.Imagetag}}
  name: {{ .Values.appConfig.appName }}
  resources:
    limits:
      memory: {{ .Values.appConfig.resourcelimit.memory }}
      cpu: {{ .Values.appConfig.resourcelimit.cpu -}}
{{ end }}

{{- define "waterlogger.deployment.envconfig" }}
env:
{{- range $key, $val := .Values.appConfig.envParams }}
{{- if $val }}
- name: {{ $key }}
  value: {{ $val | squote }}
{{ end }}{{ end }}{{ end }}

{{- define "waterlogger.deployment.commands"}}
{{- $temp := .Values.appConfig.cmds }}
command: [{{ $temp.command | quote }}]
args: [{{ $temp.args | quote }}]
{{ end }}

{{- define "waterlogger.deployment.nodeselector"}}
{{- range $key, $val := .Values.appConfig.nodeselector }}
{{ $key}}: {{ $val -}}
{{ end }}{{ end }}