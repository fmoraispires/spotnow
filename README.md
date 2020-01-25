# Spotnow
SpotNow - rent a garage now
[![version][version]]() 
* Mestrado Integrado em Engenharia Informática
* Projecto de Engenharia Informática
* SpotNow Trading Platform WebApp

## Âmbito
Há um grande problema nas cidades no que toca ao estacionamento. Não se trata de opiniões, tratam-se de factos. Factos esses que podemos ver em diversas notícias, não só em Portugal mas como no mundo inteiro. A procura é elevada, mas a oferta não consegue satisfazer o consumidor, havendo casos em que as pessoas chegam a pagar mesmo estacionando em cima da berma da estrada.
Apesar de todos os esforços, devido a imensidão do problema, a sua resolução ainda se encontra em aberto, sendo que assim esta temática apresenta um potencial elevado para exploração no contexto onde as necessidades dos consumidores sejam cumpridas.

O {SpotNow} surge como uma forma de responder a esta fragilidade que há nas cidades: falta de estacionamento.
O {SpotNow} é uma plataforma online para as pessoas anunciarem garagens, e reservarem lugares de estacionamento.
A economia partilhada, que está dar dividendos a muitas Empresas da chamada nova economia, tem uma previsão de crescimento assinalável na ordem dos 80.000 milhões em 2025, podendo o {SpotNow} ser uma das soluções neste mercado, que oferece lugares de estacionamento a um mercado de procura em crescendo. 
Uma condutor que procura um lugar para estacionar através da app do {SpotNow}, pode em tempo real consultar lugares de estacionamento fazendo a reserva, ser-lhe indicado o caminho até ao mesmo, e aceder em tempo real de forma automática a uma garagem privada.
Um proprietário de uma garagem privada, poderá através da plataforma reutilizar a sua garagem nas horas em que não está a ser usada, em especial no horário normal de trabalho, correspondente a cerca de 10 horas em que a garagem está vazia.

<img src="https://github.com/fmoraispires/spotnow/blob/master/homepage.png" width="800px">

## Arquitectura
Ao realizar um desenvolvimento ágil, a entrega de aplicativos usando um desenvolvimento monolítico, geralmente com tecnologia menos produtiva e difícil de escalar, torna-se uma tarefa quase impossível. 
Por outro lado, a necessidade de sistemas computacionais com mútliplos CPU, redes locais com centenas de hosts (dispositivos smartlocks no nosso caso), levam a uma distribuição intrínseca, numa procura por desempenho, escalabilidade, e confiabilidade.
Para resolver esse problema, adotamos um padrão de desenvolvimento de sistemas distribuídos, cliente-servidor multicamada, com broker, que se caracteriza por permitir um ambiente distribuído, heterogéneo, e com componentes cooperantes independentes, desacoplados e interoperantes.

O padrão cliente-servidor multicamadas irá assim prever a camada de frontend para a interação com o utilizador, backend com o domínio lógico do modelo de domínio, e camada de dados com o serviço de retenção de dados.

Adicionalmente o padrão broker permite obter um melhor desacoplamento entre clientes e servidores, implementando um modelo de mensagens publisher/subscribe (editores/assinantes). Este modelo é um padrão de mensagens em que os remetentes de mensagens (editores) não programam as mensagens a serem enviadas diretamente para destinatários específicos (assinantes). Em vez disso, o programador “publica” mensagens (eventos), sem o conhecimento de qualquer assinante que possa existir.
Da mesma forma, os assinantes manifestam interesse em um ou mais eventos e recebem apenas mensagens de seu interesse, sem o conhecimento de nenhum editor.
É este padrão que nos vai permitir endereçar a partir do serviço de backend os vários dispositivos smartlocks, em tempo real, para realizar as operações de acesso às garagens.

<img src="https://github.com/fmoraispires/spotnow/blob/master/deploymentspotnow.png" width="800px">


## Organização do software

O projecto apresenta a seguinte estrutura de ficheiros:

* {spotnow.frtnd} - Contém os ficheiros com informação estática, como ficheiros HTML, Javascript e CSS.

* {spotnow.bknd} - Contém a lógica de domínio e acesso à base de dados. 

* {spotnow.kubemq} - Contém a imagem docker do broker.

* {spotnow.pubs} - Contém o código de teste publisher para o broker, que depois foi adicionado ao código de backend.

* {spotnow.raspi} - Contém o código de subscriber do broker, e lógica de controlo das saídas digitais que controlam o comando de abertura do portão de garagem.


## Requisitos de Hardware e Software

|  ID   |            Software             |       Version       |                      Hardware                      |
|:-----:|:-------------------------------:|:-------------------:|:--------------------------------------------------:|
|   1   |        5.0.0-1027-azure         |  Ubuntu 18.04.3 LTS |         Standard B1ms (1 vcpus, 2 GiB memory)      |
|   2   |              kubemq             |         2.2         |                        -                           |
|   3   |              nginx              |       1.17.0        |                         -                          |
|   4   |  MySQL Community Server (GPL)   |       5.7.26        |                         -                          |
|   5   |             Docker              |       1.17.0        |                      18.09.2                       |
|   6   |         Docker-compose          |       1.25.0        |                         -                          |         
|   7   |               Vue               |       2.6.10        |                javascript framework                |
|   8   |             Django              |       2.2.0         |                  python framework                  |
|   9   | Raspbian (Linux Rasppi Debian)  |      4.19.75-v7+    |              Raspberry Pi 3 Model B+               |
|  10   |       Debian GNU/Linux 9        |  4.9.125-linuxkit   |                  (docker images)                   |
|  11   |             Python              |        3.7.3        |                         -                          |    



<!-- Markdown -->
[version]: https://img.shields.io/badge/version-3.0-brightgreen.svg
