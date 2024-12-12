-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12/12/2024 às 11:36
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `animais_esperanca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `abrigos`
--

CREATE TABLE `abrigos` (
  `id_abrigos` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `capacidade` int(5) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `abrigos`
--

INSERT INTO `abrigos` (`id_abrigos`, `nome`, `endereco`, `capacidade`, `data`) VALUES
(1, 'eldorado', 'av nestor jardim filho', 5, '2024-12-12 10:30:57');

-- --------------------------------------------------------

--
-- Estrutura para tabela `animais`
--

CREATE TABLE `animais` (
  `id_animais` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `raca` varchar(50) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `genero` char(1) NOT NULL,
  `idade` varchar(3) NOT NULL,
  `localResgatado` varchar(50) NOT NULL,
  `resgatador` varchar(50) NOT NULL,
  `abrigo` int(11) NOT NULL,
  `situacao` char(1) NOT NULL DEFAULT 'A',
  `data` timestamp NOT NULL DEFAULT current_timestamp(),
  `fk_pessoas` int(11) DEFAULT NULL,
  `fk_tutores` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `animais`
--

INSERT INTO `animais` (`id_animais`, `nome`, `raca`, `especie`, `genero`, `idade`, `localResgatado`, `resgatador`, `abrigo`, `situacao`, `data`, `fk_pessoas`, `fk_tutores`) VALUES
(3, 'nicolas', 'lindo', 'cão', 'M', '18', 'eldorado', 'eu', 1, 'A', '2024-12-12 10:31:17', NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `animais_adotados`
--

CREATE TABLE `animais_adotados` (
  `id_adotados` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `idade` varchar(3) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `raça` varchar(50) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp(),
  `fk_pessoas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `caes`
--

CREATE TABLE `caes` (
  `id_caes` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `raca` varchar(50) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `genero` char(1) NOT NULL,
  `idade` varchar(3) NOT NULL,
  `localResgatado` varchar(100) NOT NULL,
  `resgatador` varchar(100) NOT NULL,
  `abrigo` int(11) NOT NULL,
  `porte` char(1) NOT NULL,
  `cor` varchar(50) NOT NULL,
  `caracteristicas` varchar(100) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp(),
  `fk_animais` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `caes`
--

INSERT INTO `caes` (`id_caes`, `nome`, `raca`, `especie`, `genero`, `idade`, `localResgatado`, `resgatador`, `abrigo`, `porte`, `cor`, `caracteristicas`, `data`, `fk_animais`) VALUES
(1, 'nicolas', 'lindo', 'cão', 'M', '18', 'eldorado', 'eu', 1, 'M', 'branco', 'lindo', '2024-12-12 10:31:24', 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `gatos`
--

CREATE TABLE `gatos` (
  `id_gatos` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `raca` varchar(50) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `genero` char(1) NOT NULL,
  `idade` varchar(3) NOT NULL,
  `localResgatado` varchar(100) NOT NULL,
  `resgatador` varchar(100) NOT NULL,
  `abrigo` int(11) NOT NULL,
  `cor` varchar(50) NOT NULL,
  `caracteristicas` varchar(100) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp(),
  `fk_animais` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `historico`
--

CREATE TABLE `historico` (
  `id_historico` int(11) NOT NULL,
  `historico` varchar(200) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `historico`
--

INSERT INTO `historico` (`id_historico`, `historico`, `data`) VALUES
(1, 'o animal nicolas do id: 3 foi inserido', '2024-12-12 10:31:17');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pessoas`
--

CREATE TABLE `pessoas` (
  `id_pessoas` int(11) NOT NULL,
  `nome` int(11) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `senha` varchar(100) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tutores`
--

CREATE TABLE `tutores` (
  `id_tutores` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `telefone` varchar(11) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `senha` varchar(30) NOT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `abrigos`
--
ALTER TABLE `abrigos`
  ADD PRIMARY KEY (`id_abrigos`);

--
-- Índices de tabela `animais`
--
ALTER TABLE `animais`
  ADD PRIMARY KEY (`id_animais`),
  ADD KEY `fk_tutores` (`fk_tutores`),
  ADD KEY `abrigo` (`abrigo`),
  ADD KEY `fk_pessoas` (`fk_pessoas`);

--
-- Índices de tabela `animais_adotados`
--
ALTER TABLE `animais_adotados`
  ADD PRIMARY KEY (`id_adotados`),
  ADD KEY `fk_pessoas` (`fk_pessoas`);

--
-- Índices de tabela `caes`
--
ALTER TABLE `caes`
  ADD PRIMARY KEY (`id_caes`),
  ADD KEY `fk_animais` (`fk_animais`),
  ADD KEY `abrigo` (`abrigo`);

--
-- Índices de tabela `gatos`
--
ALTER TABLE `gatos`
  ADD PRIMARY KEY (`id_gatos`),
  ADD KEY `abrigo` (`abrigo`),
  ADD KEY `fk_animais` (`fk_animais`);

--
-- Índices de tabela `historico`
--
ALTER TABLE `historico`
  ADD PRIMARY KEY (`id_historico`);

--
-- Índices de tabela `pessoas`
--
ALTER TABLE `pessoas`
  ADD PRIMARY KEY (`id_pessoas`);

--
-- Índices de tabela `tutores`
--
ALTER TABLE `tutores`
  ADD PRIMARY KEY (`id_tutores`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `abrigos`
--
ALTER TABLE `abrigos`
  MODIFY `id_abrigos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `animais`
--
ALTER TABLE `animais`
  MODIFY `id_animais` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `animais_adotados`
--
ALTER TABLE `animais_adotados`
  MODIFY `id_adotados` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `caes`
--
ALTER TABLE `caes`
  MODIFY `id_caes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `gatos`
--
ALTER TABLE `gatos`
  MODIFY `id_gatos` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `historico`
--
ALTER TABLE `historico`
  MODIFY `id_historico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `pessoas`
--
ALTER TABLE `pessoas`
  MODIFY `id_pessoas` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tutores`
--
ALTER TABLE `tutores`
  MODIFY `id_tutores` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `animais`
--
ALTER TABLE `animais`
  ADD CONSTRAINT `animais_ibfk_1` FOREIGN KEY (`abrigo`) REFERENCES `abrigos` (`id_abrigos`),
  ADD CONSTRAINT `animais_ibfk_2` FOREIGN KEY (`fk_pessoas`) REFERENCES `pessoas` (`id_pessoas`),
  ADD CONSTRAINT `fk_tutores` FOREIGN KEY (`fk_tutores`) REFERENCES `tutores` (`id_tutores`);

--
-- Restrições para tabelas `animais_adotados`
--
ALTER TABLE `animais_adotados`
  ADD CONSTRAINT `animais_adotados_ibfk_1` FOREIGN KEY (`fk_pessoas`) REFERENCES `pessoas` (`id_pessoas`);

--
-- Restrições para tabelas `caes`
--
ALTER TABLE `caes`
  ADD CONSTRAINT `caes_ibfk_1` FOREIGN KEY (`fk_animais`) REFERENCES `animais` (`id_animais`),
  ADD CONSTRAINT `caes_ibfk_2` FOREIGN KEY (`abrigo`) REFERENCES `abrigos` (`id_abrigos`);

--
-- Restrições para tabelas `gatos`
--
ALTER TABLE `gatos`
  ADD CONSTRAINT `gatos_ibfk_1` FOREIGN KEY (`abrigo`) REFERENCES `abrigos` (`id_abrigos`),
  ADD CONSTRAINT `gatos_ibfk_2` FOREIGN KEY (`fk_animais`) REFERENCES `animais` (`id_animais`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
