# Spotnow
SpotNow - rent a garage now
[![version][version]]() 
* Mestrado Integrado em Engenharia Informática
* Projecto de Engenharia Informática
* SpotNow Trading Platform WebApp

## Âmbito
Ao realizar um desenvolvimento ágil, a entrega de aplicativos usando um desenvolvimento monolítico, geralmente com tecnologia menos produtiva e difícil de escalar, torna-se uma tarefa quase impossível. 
Por outro lado, a necessidade de sistemas computacionais com mútliplos CPU, redes locais com centenas de hosts (dispositivos \textit{smartlocks} no nosso caso), levam a uma distribuição intrínseca, numa procura por desempenho, escalabilidade, e confiabilidade.
Para resolver esse problema, adotamos um padrão de desenvolvimento de sistemas distribuídos, cliente-servidor multicamada, com broker, que se caracteriza por permitir um ambiente distribuído, heterogéneo, e com componentes cooperantes independentes, desacoplados e interoperantes.

O padrão cliente-servidor multicamadas irá assim prever a camada de frontend para a interação com o utilizador, backend com o domínio lógico do modelo de domínio, e camada de dados com o serviço de retenção de dados.

Adicionalmente o padrão \textit{broker} permite obter um melhor desacoplamento entre clientes e servidores, implementando um modelo de mensagens publisher/subscribe (editores/assinantes). Este modelo é um padrão de mensagens em que os remetentes de mensagens (editores) não programam as mensagens a serem enviadas diretamente para destinatários específicos (assinantes). Em vez disso, o programador “publica” mensagens (eventos), sem o conhecimento de qualquer assinante que possa existir.
Da mesma forma, os assinantes manifestam interesse em um ou mais eventos e recebem apenas mensagens de seu interesse, sem o conhecimento de nenhum editor.
É este padrão que nos vai permitir endereçar a partir do serviço de \textit{backend} os vários dispositivos \textit{smartlocks}, em tempo real, para realizar as operações de acesso às garagens.

## Conteúdo


## Setup


## Organização do software

O projecto apresenta a seguinte estrutura de ficheiros:

* {spotnow.frtnd} - Contém os ficheiros com informação estática, como ficheiros HTML, Javascript (jQuery para Bootstrap), e CSS.

* {spotnow.bknd} - Contém a lógica de domínio e acesso à base de dados. 

* {spotnow.kubemq} - Contém a imagem do broker.

* {spotnow.pubs} - Contém o código de teste publisher para o broker, que depois foi adicionado ao código de backend.

* {spotnow.raspi} - Contém o código de subscriber do broker, e lógica de controlo das saídas digitais que controlam o comando de abertura do portão de garagem.


## Requisitos de Software

|  ID   |            Software             |       Version       |                      Hardware                      |
|:-----:|:-------------------------------:|:-------------------:|:--------------------------------------------------:|
|   1   |              MacOS              |   Mojave 10.14.6    |  1,4 GHz Intel Core i5, 8 GB RAM 2133 MHz   DDR3   |
|   2   |           Dotnet core           |         3.0         |                 512MB RAM, 64-bit                  |
|   3   |              nginx              |       1.17.0        |                         -                          |
|   4   |  MySQL Community Server (GPL)   |       5.7.26        |                         -                          |
|   5   |             Docker              |       1.17.0        |                      18.09.2                       |
|   6   |       Debian GNU/Linux 9        |  4.9.125-linuxkit   |                  (docker images)                   |



<!-- Markdown -->
[version]: https://img.shields.io/badge/version-7.0-brightgreen.svg
